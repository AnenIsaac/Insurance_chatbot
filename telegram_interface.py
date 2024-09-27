import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv() # will search for .env file in local folder and load variables 

TOKEN = os.getenv('TELEGRAM_TOKEN') 


CHATBOT_SCRIPT = r'simple_chatbot.py'

# Store active chatbot processes
active_chats = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    logger.info(f"User {user_id} started the bot")

    # Start the chatbot process using asyncio's subprocess
    process = await asyncio.create_subprocess_exec(
        'python', CHATBOT_SCRIPT,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    active_chats[user_id] = process

    # Read the initial output from the chatbot (main menu)
    initial_output = await read_output(process)
    await update.message.reply_text(initial_output)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_input = update.message.text
    logger.info(f"Received message from user {user_id}: {user_input}")

    if user_id not in active_chats:
        await update.message.reply_text("Please start the chat using /start command.")
        return

    process = active_chats[user_id]

    try:
        # Send user input to the chatbot
        process.stdin.write(f"{user_input}\n".encode('utf-8'))  # Encode input as bytes
        await process.stdin.drain()  # Ensure data is sent

        # Read the output from the chatbot
        chatbot_response = await read_output(process)

        if chatbot_response:
            await update.message.reply_text(chatbot_response)
        else:
            await update.message.reply_text("The chatbot has ended the conversation.")
            await end_chat(user_id)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        await update.message.reply_text("the chat has ended. Send /start to restart the chat")
        await end_chat(user_id)


async def read_output(process, timeout=5):
    """Read the output from the chatbot process asynchronously."""
    output = b""  # Initialize as byte string
    try:
        while True:
            line = await asyncio.wait_for(process.stdout.readline(), timeout=timeout)
            if not line:
                break
            output += line
    except asyncio.TimeoutError:
        # No more output expected within the timeout
        pass

    return output.decode('utf-8').strip()  # Decode byte string to UTF-8 text


async def end_chat(user_id):
    """End the chatbot session for a user."""
    if user_id in active_chats:
        process = active_chats[user_id]
        process.terminate()
        await process.wait()  # Ensure the process ends
        del active_chats[user_id]


def main():
    """Run the bot."""
    logger.info("Starting the bot...")
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Webhook setup
    application.run_webhook(
        listen="0.0.0.0",  # Listen on all interfaces
        port=int(os.environ.get("PORT", 8443)),  # Use the PORT environment variable
        url_path=TOKEN,  # The URL path should include your bot token
        webhook_url=f"https://insurancechatbot-production.up.railway.app/{TOKEN}"  # Corrected webhook URL
    )


if __name__ == '__main__':
    main()
