import re
from datetime import datetime
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')



user_data = {

}


def main_menu():
    """Main Menu"""
    print("Karibu BimaChap\n")
    print("1. Bima Ndogo (Third Party) 🏍🚗")
    print("2. Dereva Kipato (Drivers) 🩼🦽")
    print("3. Bima ya Safari (Travel) ✈️🌍")
    print("4. Vigezo na masharti")
    print("5. Ofisi zetu (Our offices)")

    choice = input("Chagua chaguo (Choose an option): \n")

    if choice == '1':
        user_data["insurance_type"] = 'Bima Ndogo'
        bima_ndogo_menu()
    elif choice == '2':
        user_data["insurance_type"] = 'Dereva Kipato'
        dereva_kipato_menu()
    elif choice == '3':
        user_data["insurance_type"] = 'Bima ya Safari'
        bima_ya_safari_menu()
    elif choice == '4':
        vigezo_na_masharti_menu()
    elif choice == '5':
        ofisi_zetu_menu()
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        main_menu()  # Show the menu again
# 
# 
# 
# functions for other menus
def bima_ndogo_menu():
    """Main menu -> Bima Ndogo (Third Party)"""
    print("Bima Ndogo (Third Party) 🏍🛺🚜🚛🚌🚕🚗🚙\n")
    print("1. Nunua")
    print("2. Angalia Bei")
    print("3. Madai")
    print("4. Jisajili kukumbushwa")
    print("5. Huduma kwa wateja")
    print("\n# - Rudi menyu kuu")

    choice = input("Chagua chaguo (Choose an option): \n")

    if choice == '1':
        nunua()
    elif choice == '2':
        angalia_bei()
    elif choice == '3':
        madai_menu
    elif choice == '4':
        jisajili_kukumbushwa()
    elif choice == '5':
        huduma_kwa_wateja()
    elif choice == '#':
        main_menu()  # Go back to the main menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        bima_ndogo_menu()  # Show the menu again

# functions for the actions in the Bima Ndogo menu
# START OF BIMA NDOGO -> 1. NUNUA FLOW
def nunua():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua"""
    print("Ingiza namba ya gari/chombo (mfano T 257 CWU au XX123ABC)\n")
    print("# - Kurudi nyuma")

    vehicle_number = input("Ingiza namba ya gari/chombo: \n").strip().replace(" ", "").upper()

    if vehicle_number == '#':
        bima_ndogo_menu()  # Go back to the previous menu
    else:
        # Updated pattern to allow any two letters instead of "MC"
        pattern = r'^(T\d{3}[A-Z]{3}|[A-Z]{2}\d{3}[A-Z]{3}|T \d{3} [A-Z]{3})$'

        if re.match(pattern, vehicle_number):
            user_data["vehicle_number"] = vehicle_number
            print(f"Namba ya gari/chombo uliyoiingiza ni: {user_data['vehicle_number']}")
            matumizi_ya_gari_menu()  # Go to the next step
        else:
            print("Namba ya gari/chombo si sahihi. Tafadhali jaribu tena.")
            nunua()

def matumizi_ya_gari_menu():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Matumizi ya gari"""
    print("Matumizi ya gari ni:\n")
    print("1. Binafsi")
    print("2. Biashara - Kubeba abiria")
    print("3. Biashara - Kubeba mizigo")
    print("\n# - Kurudi nyuma")

    choice = input("Chagua chaguo (Choose an option): \n")

    if choice == '1':
        user_data["matumizi_ya_gari"] = "Binafsi"
        ingiza_majina_yako()
    elif choice == '2':
        user_data["matumizi_ya_gari"] = "Biashara - Kubeba abiria"
        ingiza_majina_yako()
    elif choice == '3':
        user_data["matumizi_ya_gari"] = "Biashara - Kubeba mizigo"
        ingiza_majina_yako()
    elif choice == '#':
        nunua()  # Go back to the Nunua menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        matumizi_ya_gari_menu()  # Show the menu again

# Placeholder functions for each option in the usage menu
def ingiza_majina_yako():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Binafsi -> Ingiza majina yako"""
    print("Ingiza majina yako kamili\n")
    print("# - Kurudi nyuma")

    full_name = input("Ingiza majina yako kamili: \n").strip()

    if full_name == '#':
        matumizi_ya_gari_menu()  # Go back to the previous menu
    else:
        # Check if at least two names are provided
        names = full_name.split()

        if len(names) >= 2:
            user_data["full_name"] = full_name
            print(f"Majina uliyoiingiza ni: {user_data['full_name']}")
            hakiki_usahihi_menu()  # Proceed to the next menu
        else:
            print("Tafadhali ingiza majina angalau mawili.")
            ingiza_majina_yako()  # Retry input if less than two names


def hakiki_usahihi_menu():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Binafsi -> Ingiza majina yako -> Hakiki usahihi"""
    print("HAKIKI USAHIHI WA TAAFIRA ULIZOWEKA:\n")
    print("Usajili wa gari:")
    # Placeholder for displaying the vehicle registration number
    print(f"Namba ya gari: {user_data['vehicle_number']}")  # Assuming vehicle_number is defined globally
    print("Aina ya gari: [Placeholder for vehicle type]")  # You can replace this with actual data
    print("Muda wa bima: [Placeholder for insurance duration]")  # Replace with actual data
    print("Kiasi: [Placeholder for amount]")  # Replace with actual data

    print("\nThibitisha unalipa kabla ya ajali\n")
    print("1. Endelea")
    print("2. Sahihisha")
    print("3. Sitisha")
    print("\n# - Kurudi nyuma")

    choice = input("Chagua chaguo (Choose an option): \n")

    if choice == '1':            
        endelea()  # Function to handle continuation
    elif choice == '2':
        nunua()  # Function to handle correction
    elif choice == '3':
        sitisha()  # Function to handle cancellation
    elif choice == '#':
        ingiza_majina_yako()  # Go back to the Binafsi menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        hakiki_usahihi_menu()  # Show the menu again

# Placeholder functions for each option
def endelea():
    bima_unayo_nunua_menu()

def sahihisha():
    nunua()

def sitisha():
    main_menu()

# You can call hakiki_usahihi_menu() when needed
def bima_unayo_nunua_menu():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Binafsi -> Ingiza majina yako -> Hakiki usahihi -> bima unayo nunua"""
    print("Je bima unayo nunua ni:\n")
    print("1. Yako")
    print("2. Ya mwingine")
    print("\n# - Kurudi nyuma")

    choice = input("Chagua chaguo (Choose an option): \n")

    if choice == '1':
        user_data["insurance_for"] = "Binafsi"
        mmiliki_wa_gari()  # Function to handle "Yako"
    elif choice == '2':
        user_data["insurance_for"] = "Mwingine"
        ya_mwingine()  # Function to handle "Ya mwingine"
    elif choice == '#':
        hakiki_usahihi_menu()  # Go back to the Hakiki Usahihi menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        bima_unayo_nunua_menu()  # Show the menu again

# Placeholder functions for each option
def mmiliki_wa_gari():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Binafsi -> Ingiza majina yako -> Hakiki usahihi -> bima unayo nunua (binafsi) -> mmiliki wa gari"""
    print("Je mmiliki wa gari ni:\n")
    print("1. Mtu binafsi")
    print("2. Kampuni")
    print("\n# - Kurudi nyuma")

    choice = input("Chagua chaguo (Choose an option): \n")

    if choice == '1':
        user_data["owner_of_car"] = 'Mtu binafsi'
        chagua_mfumo_wa_malipo()  # Function to handle "Mtu binafsi"
    elif choice == '2':
        user_data["owner_of_car"] = 'Kampuni'
        ingiza_tin_ya_kampuni()  # Function to handle "Kampuni"
    elif choice == '#':
        bima_unayo_nunua_menu()  # Go back to the Bima Unayo Nunua menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        mmiliki_wa_gari()  # Show the menu again

# Placeholder functions for each option
def chagua_mfumo_wa_malipo():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Binafsi -> Ingiza majina yako -> Hakiki usahihi -> bima unayo nunua (yako) -> mmiliki wa gari (mtu binafsi)-> Payment"""
    print("Chagua mfumo wa malipo\n")
    print("1. Tigo Pesa")
    print("2. Mpesa")
    print("3. Airtel Money")
    print("4. Kumbukumbu namba")
    print("# - Kurudi nyuma")

    choice = input("Chagua mfumo wa malipo: \n").strip()

    if choice == '#':
        mmiliki_wa_gari()  # Go back to the previous menu
    else:
        if choice == '1':
            print("Umechagua Tigo Pesa.")
            # Handle the Tigo Pesa payment flow here
        elif choice == '2':
            print("Umechagua Mpesa.")
            # Handle the Mpesa payment flow here
        elif choice == '3':
            print("Umechagua Airtel Money.")
            # Handle the Airtel Money payment flow here
        elif choice == '4':
            print("Umechagua Kumbukumbu namba.")
            # Handle the reference number flow here
        else:
            print("Chaguo sio sahihi. Tafadhali chagua tena.")
            chagua_mfumo_wa_malipo()  # Retry if input is invalid

# Call chagua_mfumo_wa_malipo() for testing


def ingiza_tin_ya_kampuni():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Binafsi -> Ingiza majina yako -> Hakiki usahihi -> bima unayo nunua (yako) -> mmiliki wa gari (kampuni)-> ingiza TIN"""
    print("Ingiza TIN namba ya kampuni\n")
    print("Mfano: 123456789")
    print("# - Kurudi nyuma")

    tin_number = input("Ingiza TIN namba ya kampuni: \n").strip()

    if tin_number == '#':
        mmiliki_wa_gari()  # Go back to the previous menu
    else:
        # Check if the input matches the TIN number format (9 digits)
        if re.match(r'^\d{9}$', tin_number):
            user_data["company_tin_number"] = tin_number
            print(f"TIN namba ya kampuni uliyoiingiza ni: {user_data['company_tin_number']}")
            chagua_mfumo_wa_malipo()  # Proceed to the next step
        else:
            print("TIN namba si sahihi. Tafadhali jaribu tena.")
            ingiza_tin_ya_kampuni()  # Retry if the input is incorrect



# You can call mmiliki_wa_gari() when needed

def ya_mwingine():
    """Main menu -> Bima Ndogo (Third Party) -> Nunua (ingiza namba ya gari) -> Binafsi -> Ingiza majina yako -> Hakiki usahihi -> bima unayo nunua -> ya mwingine"""
    print("Ingiza namba yake sahihi ya simu ya mkononi\n")
    print("Mfano: 07XX XXX XXX au 07XXXXXXXX")
    print("# - Kurudi nyuma")

    phone_number = input("Ingiza namba ya simu: \n").strip()

    if phone_number == '#':
        bima_unayo_nunua_menu()  # Go back to the previous menu
    else:
        # Remove any whitespaces in the phone number
        phone_number = phone_number.replace(" ", "")

        # Validate if the phone number matches the format (10 digits starting with 06 or 07)
        if re.match(r'^0[67]\d{8}$', phone_number):
            user_data["applicant_phone_number"] = phone_number
            print(f"Namba ya simu uliyoiingiza ni: {user_data['applicant_phone_number']}")
            mmiliki_wa_gari()  # Proceed to the next step
        else:
            print("Namba ya simu si sahihi. Tafadhali jaribu tena.")
            ya_mwingine()  # Retry if the input is incorrect

# You can call bima_unayo_nunua_menu() when needed
# END OF BIMA NDOGO -> 1. NUNUA FLOW

# START OF BIMA NDOGO -> 2. ANGALIA BEI FLOW
def angalia_bei():
    """Main menu -> Angalia bei"""
    print("Ingiza namba ya gari/chombo\n")
    print("(mfano T100ABC au MC123ABC)")
    print("# - Kurudi nyuma")

    vehicle_number = input("Ingiza namba ya gari/chombo: \n").strip().replace(" ", "").upper()

    if vehicle_number == '#':
        bima_ndogo_menu()  # Go back to the previous menu
    else:
        # Updated pattern to allow any two letters instead of "MC"
        pattern = r'^(T\d{3}[A-Z]{3}|[A-Z]{2}\d{3}[A-Z]{3}|T \d{3} [A-Z]{3})$'

        if re.match(pattern, vehicle_number):
            user_data["vehicle_number"] = vehicle_number
            print(f"Namba ya gari/chombo uliyoiingiza ni: {user_data['vehicle_number']}")
            matumizi_ya_gari_menu_angalia_bei()  # Go to the next step
        else:
            print("Namba ya gari/chombo si sahihi. Tafadhali jaribu tena.")
            nunua()

def matumizi_ya_gari_menu_angalia_bei():
    """Main menu -> Angalia bei -> Matumizi ya gari"""
    print("Matumizi ya gari ni:\n")
    print("1. Binafsi")
    print("2. Biashara - Kubeba abiria")
    print("3. Biashara - Kubeba mizigo")
    print("\n# - Kurudi nyuma")

    choice = input("Chagua chaguo (Choose an option): \n")

    if choice == '1':
        user_data["matumizi_ya_gari"] = "Binafsi"
        muhtasari_wa_bei()
    elif choice == '2':
        user_data["matumizi_ya_gari"] = "Biashara - Kubeba abiria"
        muhtasari_wa_bei()
    elif choice == '3':
        user_data["matumizi_ya_gari"] = "Biashara - Kubeba mizigo"
        muhtasari_wa_bei()
    elif choice == '#':
        angalia_bei() 
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        matumizi_ya_gari_menu()  # Show the menu again 
        

def muhtasari_wa_bei():
    """Main menu -> Angalia bei -> Matumizi ya gari -> Muhtasari wa bei"""
    # Displaying the summary based on the user's entered data
    print("\nMuhtasari wa bei ya bima\n")
    print(f"*Usajili wa chombo*: {user_data['vehicle_number']}")
    print(f"*Matumizi*: {user_data['matumizi_ya_gari']}")
    print("*Kiasi*: [placeholder for insurance amount]")
    print("*Muda wa Bima*: [placeholder for insurance time]")
    
    print("\n1. Kuendelea kununua")
    print("2. Angalia bei ya Gari lingine")
    print("# - Rudi menyu kuu")

    # Get user input for next step
    choice = input("Chagua moja: \n").strip()

    if choice == "1":
        # Proceed to purchase
        ingiza_majina_yako()  # Next step in the process
    elif choice == "2":
        # Go back to check the price for another car
        angalia_bei()  # Re-enter the vehicle number and check price again
    elif choice == "#":
        main_menu()  # Return to the main menu
    else:
        print("Chaguo sio sahihi. Tafadhali jaribu tena.")
        muhtasari_wa_bei(user_data)  # Show the summary again
# You can call the matumizi_ya_gari_menu() function when needed



def madai_menu():
    """Main menu -> Bima Ndogo -> Madai menu"""
    print("\nJe unawasilisha taarifa za madai...\n")
    print("1.⁠ Ukiwa mteja wa BimaChap")
    print("\nAU\n")
    print("2.⁠ Dhidi ya mteja wa BimaChap")
    print("\n# - Rudi nyuma")
    
    # Get user input
    choice = input("Chagua moja: \n").strip()

    if choice == "1":
        # Call the function for claims as a BimaChap client
        madai_mteja()
    elif choice == "2":
        # Call the function for claims against a BimaChap client
        madai_dhidi_ya_mteja()
    elif choice == "#":
        bima_ndogo_menu()  # Go back to the previous menu
    else:
        print("Chaguo sio sahihi. Tafadhali jaribu tena.")
        madai_menu()  # Reload the claims menu for incorrect input

# Placeholder functions for next steps
def madai_mteja():
    """Main menu -> Bima Ndogo -> Madai menu -> mteja wa BimaChap"""
    print("\nJe unatoa taarifa hizi kama...\n")
    print("1. Mmiliki")
    print("2. Mwakilishi rasmi wa Mmiliki")
    print("\n# - Rudi nyuma")

    # Get user input
    choice = input("Chagua moja: \n").strip()

    if choice == "1":
        # Proceed with the claim as the owner
        madai_mmiliki()
    elif choice == "2":
        # Proceed with the claim as a representative of the owner
        madai_mwakilishi_rasmi()
    elif choice == "#":
        madai_menu()  # Go back to the previous menu
    else:
        print("Chaguo sio sahihi. Tafadhali jaribu tena.")
        madai_mteja()  # Reload the menu for incorrect input

# Placeholder functions for next steps
def madai_mmiliki():
    """Main menu -> Bima Ndogo -> Madai menu -> mteja wa BimaChap -> Mmiliki"""
    print("\nKwa mawasiliano, taja namba ya simu yako ya kiganjani inayopatikana kiurahisi.")
    print("\n# - Rudi nyuma")

    phone_number = input("Ingiza namba ya simu: \n").strip().replace(" ", "")

    if phone_number == "#":
        madai_mteja()  # Go back to the previous menu
    else:
        # Validate the phone number format (Tanzanian format: starts with '07' or '06', followed by 8 digits)
        pattern = r'^(07\d{8}|06\d{8})$'

        if re.match(pattern, phone_number):
            user_data["madai_mteja_phone_number"] = phone_number
            print(f"Namba ya simu uliyoiweka ni: {user_data["madai_mteja_phone_number"]}")
            # Proceed to the next step
            thibitisha_madai(phone_number)
        else:
            print("Namba ya simu si sahihi. Tafadhali jaribu tena.")
            madai_mmiliki()  # Reload if the number is incorrect


def madai_mwakilishi_rasmi():
    """Main menu -> Bima Ndogo -> Madai menu -> mteja wa BimaChap -> Mwakilishi"""
    print("\nKwa mawasiliano, taja namba ya simu yako ya kiganjani inayopatikana kiurahisi.")
    print("\n# - Rudi nyuma")

    phone_number = input("Ingiza namba ya simu: \n").strip().replace(" ", "")

    if phone_number == "#":
        madai_mteja()  # Go back to the previous menu
    else:
        # Validate the phone number format (Tanzanian format: starts with '07' or '06', followed by 8 digits)
        pattern = r'^(07\d{8}|06\d{8})$'

        if re.match(pattern, phone_number):
            user_data["madai_mwakilishi_phone_number"] = phone_number
            print(f"Namba ya simu uliyoiweka ni: {user_data["madai_mwakilishi_phone_number"]}")
            # Proceed to the next step
            thibitisha_madai(phone_number)
        else:
            print("Namba ya simu si sahihi. Tafadhali jaribu tena.")
            madai_mmiliki()  # Reload if the number is incorrect

def thibitisha_madai(phone_number):
    """Main menu -> Bima Ndogo -> Madai menu -> mteja wa BimaChap -> Mmiliki -> Thibitsha"""
    print(f"Madai yako yamewasilishwa kikamilifu. Tutawasiliana na wewe kupitia namba ya simu uliyosajili: {phone_number}.")
    print("Asante kwa kutumia huduma zetu za BimaChap.")
    
def madai_dhidi_ya_mteja():
    """Main menu -> Bima Ndogo -> Madai menu -> Dhidi ya mteja wa BimaChap"""
    print("Kwa madai dhidi ya mteja wa BimaChap tafadhali wasiliana na mteja wetu ili kukamilisha taratibu za madai. \nAsante kwa kutumia BimaChap")
    
def jisajili_kukumbushwa():
    """Main menu -> Bima Ndogo -> Jisajili Kukumbushwa"""
    print("\nIngiza namba ya gari/chombo")
    print("mfano (T100ABC au MC123ABC)")
    print("\n# - Kurudi nyuma")

    vehicle_number = input("Ingiza namba ya gari/chombo: \n").strip().replace(" ", "").upper()

    if vehicle_number == "#":
        bima_ndogo_menu()  # Go back to the previous menu
    else:
        # Validate vehicle number format
        pattern = r'^(T\d{3}[A-Z]{3}|[A-Z]{2}\d{3}[A-Z]{3})$'

        if re.match(pattern, vehicle_number):
            user_data["vehicle_number"] = vehicle_number
            print(f"Namba ya gari uliyoiweka ni: {user_data['vehicle_number']}")
            tarehe_ya_bima_kuisha()
        else:
            print("Namba ya gari si sahihi. Tafadhali jaribu tena.")
            jisajili_kukumbushwa()  # Reload the menu for a valid entry
            
def tarehe_ya_bima_kuisha():
    """Main menu -> Bima Ndogo -> Jisajili Kukumbushwa -> Tarehe ya Bima Kuisha"""
    print("\nIngiza tarehe ya bima kuisha (YYYY-MM-DD)")
    print("MWAKA-MWEZI-SIKU\nmfano: 2020-04-25")
    print("\n# - Kurudi nyuma")

    insurance_end_date = input("Ingiza tarehe ya bima kuisha (YYYY-MM-DD): \n").strip()

    if insurance_end_date == "#":
        jisajili_kukumbushwa()  # Go back to the previous menu
    else:
        try:
            # Validate if the entered date is in the correct format
            date_obj = datetime.datetime.strptime(insurance_end_date, '%Y-%m-%d')
            today = datetime.datetime.now()

            # Check if the date entered is in the future
            if date_obj >= today:
                user_data["insurance_end_date"] = insurance_end_date
                print(f"Tarehe ya bima kuisha uliyoweka ni: {user_data['insurance_end_date']}")
                usajili_umekamilika()
            else:
                print("Tarehe uliyoweka iko nyuma ya siku ya leo. Tafadhali jaribu tena.")
                tarehe_ya_bima_kuisha()  # Reload for a valid date

        except ValueError:
            print("Tarehe si sahihi. Tafadhali weka kwa mfumo wa YYYY-MM-DD.")
            tarehe_ya_bima_kuisha()  # Reload the function for correct input
            
def usajili_umekamilika():
    """Display confirmation and check input for returning to the main menu or exiting."""
    print("\nUsajili umekamilika.")
    print("Utakumbushwa bima ikikaribia kuisha muda wake.")
    print("Endelea kufurahia huduma zetu.")
    print("\nTuma # kurudi menyu kuu.")
    
    choice = input("Ingiza #: \n")

    if choice == '#':
        main_menu()  # Go back to the main menu
    else:
        print("Asante kwa kutumia huduma zetu.")
        exit()  # Exit the system
    
def huduma_kwa_wateja():
    """Main menu -> Bima Ndogo -> Huduma kwa Wateja"""
    print("\nHuduma")
    print("1. Hakiki bima yako")
    print("2. Kufahamu stika ya bima")
    print("3. Kujua bima yangu inaisha lini")
    print("\n# - Kurudi nyuma")

    choice = input("Chagua huduma: \n")

    if choice == '1':
        hakiki_bima_ya_safari_yako()
    elif choice == '2':
        fahamu_stika_ya_bima()
    elif choice == '3':
        kujua_bima_inaisha_lini()
    elif choice == '#':
        bima_ndogo_menu()  # Go back to Bima Ndogo menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        huduma_kwa_wateja()  # Show the menu again
        
def hakiki_bima_ya_safari_yako():
    """Main menu -> Bima Ndogo -> Huduma kwa Wateja -> Hakiki Bima Yako"""
    print("\nBofya: https://mis.tira.go.tz/auth/validateCover")
    print("Asante kwa kutumia BimaChap.")
    print("\nTuma # kurudi menyu kuu.")
    
    choice = input("Ingiza #: \n")

    if choice == '#':
        main_menu()  # Go back to the main menu
    else:
        print("Asante kwa kutumia huduma zetu.")
        exit()  # Exit the system
        
def fahamu_stika_ya_bima():
    """Main menu -> Bima Ndogo -> Huduma kwa Wateja -> Kufahamu Stika ya Bima"""
    print("\nBofya https://mis.tira.go.tz/auth/validateCover")
    print("Asante kwa kutumia BimaChap.")
    print("\nTuma # kurudi menyu kuu.")
    
    choice = input("Ingiza #: \n")

    if choice == '#':
        main_menu()  # Go back to the main menu
    else:
        print("Asante kwa kutumia huduma zetu.")
        exit()  # Exit the system

def kujua_bima_inaisha_lini():
    """Main menu -> Bima Ndogo -> Huduma kwa Wateja -> Kujua Bima Inaisha Lini"""
    print("\nBofya https://mis.tira.go.tz/auth/validateCover")
    print("Asante kwa kutumia BimaChap.")
    print("\nTuma # kurudi menyu kuu.")
    
    choice = input("Ingiza #: \n")

    if choice == '#':
        main_menu()  # Go back to the main menu
    else:
        print("Shukrani kwa kutumia huduma zetu.")
        exit()  # Exit the system

def dereva_kipato_menu():
    """Main menu -> Dereva Kipato"""
    print("\nDereva Kipato (Ajali)\n")
    print("1. Nunua")
    print("2. Hakiki bima")
    print("3. Madai")
    print("\n# - Rudi menyu kuu")
    
    choice = input("Chagua chaguo: \n").strip()
    
    if choice == '1':
        nunua_dereva_kipato()
    elif choice == '2':
        hakiki_bima()
    elif choice == '3':
        dereva_kipato_madai_menu()
    elif choice == '#':
        main_menu()  # Go back to the main menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        dereva_kipato_menu()  # Show the menu again

def nunua_dereva_kipato():
    """Main menu -> Dereva Kipato Nunua"""
    print("\nIngiza namba ya LESENI ya udereva ya Tanzania")
    print("# - Rudi nyuma")
    
    license_number = input("Ingiza namba ya LESENI: \n").strip()

    if license_number == '#':
        dereva_kipato_menu()  # Go back to the previous menu
    else:
        # Here you can add checks to validate the license number if necessary
        # For example, you could validate the format of the license number
        if validate_license_number(license_number):  # Define this function as needed
            user_data["license_number"] = license_number
            print(f"Namba ya LESENI uliyoiingiza ni: {user_data['license_number']}")
            # Proceed to the next step or menu
            andika_jina_la_kwanza()
        else:
            print("Namba ya LESENI si sahihi. Tafadhali jaribu tena.")
            nunua_dereva_kipato()  # Show the menu again

def validate_license_number(license_number): 
    """Function to validate tanzanian license number"""
    if license_number:
        return True
    else:
        False
        
def andika_jina_la_kwanza():
    """Dereva Kipato -> Nunua -> Andika Jina la Kwanza"""
    print("\nAndika jina la *KWANZA* kama ilivyo kwenye leseni ya udereva")
    print("# - Rudi nyuma")
    
    first_name = input("Ingiza jina la Kwanza: \n").strip()

    if first_name == '#':
        nunua_dereva_kipato()  # Go back to the previous menu
    else:
        if len(first_name.split()) == 1: 
            user_data["first_name"] = first_name
            print(f"Jina la Kwanza uliyoiingiza ni: {user_data['first_name']}")
            # Proceed to the next step or menu
            andika_jina_la_ukoo()
        else:
            print("Umeengiza majina zaidi ya mmoja, tafadhali ingiza jina la kwanza tu.")
            andika_jina_la_kwanza()  # Show the menu again
            
def andika_jina_la_ukoo():
    """Dereva Kipato -> Nunua -> Andika Jina la Kwanza -> Andika Jina la Ukoo"""
    print("\nAndika jina la *UKOO* kama ilivyo kwenye leseni ya udereva")
    print("# - Rudi nyuma")
    
    surname = input("Umeengiza majina zaidi ya mmoja, tafadhal ingiza jina la Ukoo tu: \n").strip()

    if surname == '#':
        andika_jina_la_kwanza()  # Go back to the previous menu
    else:
        if len(surname.split()) == 1:  # Check if at least one name is provided
            user_data["surname"] = surname
            print(f"Jina la Ukoo uliyoiingiza ni: {user_data['surname']}")
            # Proceed to the next step or menu
            ingiza_tarehe_ya_kutolewa_leseni()
        else:
            print("Tafadhali andika jina la Ukoo tu.")
            andika_jina_la_ukoo()  # Show the menu again

def ingiza_tarehe_ya_kutolewa_leseni():
    """Main Menu -> Dereva Kipato -> Nunua -> Andika Jina la Kwanza -> Andika Jina la Ukoo -> Ingiza Tarehe ya Kutolewa kwa Leseni ya Udereva"""
    print("\nIngiza Tarehe ya Kutolewa kwa leseni ya udereva")
    print(" *SIKU/MWEZI/MWAKA*")
    print("mfano: 28/02/2023")
    print("# - Rudi nyuma")
    
    license_issuance_date = input("Ingiza tarehe ya kutolewa: \n").strip()

    if license_issuance_date == '#':
        andika_jina_la_ukoo()  # Go back to the previous menu
    else:
        # You can add a regex or validation here to check date format
        pattern = r'^\d{1,2}/\d{1,2}/\d{4}$'  # Matches DD/MM/YYYY format

        if re.match(pattern, license_issuance_date):
            user_data["license_issuance_date"] = license_issuance_date
            print(f"Tarehe ya kutolewa uliyoiingiza ni: {user_data['license_issuance_date']}")
            # Proceed to the next step or menu
            muda_wa_bima_menu()
        else:
            print("Tafadhali ingiza tarehe kwa muundo sahihi: SIKU/MWEZI/MWAKA, mfano: 28/02/2023.")
            ingiza_tarehe_ya_kutolewa_leseni()  # Show the menu again

def muda_wa_bima_menu():
    """Main Menu -> Dereva Kipato -> Nunua -> Andika Jina la Kwanza -> Andika Jina la Ukoo -> Ingiza Tarehe ya Kutolewa kwa Leseni ya Udereva -> Chagua muda wa bima"""
    print("\nChagua muda wa bima")
    print("1. Mwaka 1")
    print("2. Miezi 3")
    print("3. Mwezi 1")
    print("4. Wiki 1")
    print("5. Siku 3")
    print("#. Rudi nyuma")
    
    choice = input("Ingiza chaguo lako: \n").strip()

    if choice == '#':
        ingiza_tarehe_ya_kutolewa_leseni()  # Go back to the previous menu
    elif choice == '1':
        user_data["muda_wa_bima"] = 'Mwaka 1'
        print("Umechagua Mwaka 1")
        # Handle the duration choice (e.g., store it in user_data)
    elif choice == '2':
        user_data["muda_wa_bima"] = 'Miezi 3'
        print("Umechagua Miezi 3")
        # Handle the duration choice
    elif choice == '3':
        user_data["muda_wa_bima"] = 'Mwezi 1'
        print("Umechagua Mwezi 1")
        # Handle the duration choice
    elif choice == '4':
        user_data["muda_wa_bima"] = 'Wiki 1'
        print("Umechagua Wiki 1")
        # Handle the duration choice
    elif choice == '5':
        user_data["muda_wa_bima"] = 'Siku 3'
        print("Umechagua Siku 3")
        # Handle the duration choice
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        muda_wa_bima_menu()  # Retry the menu
    thamani_ya_bima_menu()
def thamani_ya_bima_menu():
    """Main Menu -> Dereva Kipato -> Nunua -> Andika Jina la Kwanza -> Andika Jina la Ukoo -> Ingiza Tarehe ya Kutolewa kwa Leseni ya Udereva -> Chagua muda wa bima -> Ingiza thamani ya kinga ya bima"""
    print("\nIngiza thamani ya kinga ya bima")
    print("#. Rudi nyuma")

    value = input("Ingiza thamani ya kinga ya bima: \n").strip()

    if value == '#':
        muda_wa_bima_menu()  # Go back to the previous menu
    else:
        try:
            # Convert the input to a float, if necessary
            coverage_value = float(value.replace(",", "").strip())  # Handle commas in numbers
            print(f"Thamani ya kinga ya bima uliyoiingiza ni: {coverage_value}")
            # Proceed to the next step or store the value in user_data
        except ValueError:
            print("Thamani si sahihi. Tafadhali ingiza nambari sahihi.")
            thamani_ya_bima_menu()  # Retry the menu
            
def bei_ya_bima_menu():
    """Main Menu -> Dereva Kipato -> Nunua -> Andika Jina la Kwanza -> Andika Jina la Ukoo -> Ingiza Tarehe ya Kutolewa kwa Leseni ya Udereva -> Chagua muda wa bima -> Ingiza thamani ya kinga ya bima -> Bei ya bima"""
    print("\n*BEI: 69,384*")
    print("\n*Fidia Vikomo*")
    print("Kulazwa: 6,000,000")
    print("Kipato @Wiki: 57,692 *kwa wiki 104*")
    print("Ulemavu: 12,000,000")
    print("Na: Malazi, Usafiri, Leseni Kupotea")
    print("\n1. LIPA")
    print("#. Rudi nyuma")

    choice = input("Chagua chaguo lako: \n").strip()

    if choice == '1':
        chagua_mfumo_wa_malipo()  # Function to handle payment process
    elif choice == '#':
        thamani_ya_bima_menu()  # Go back to the previous menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        bei_ya_bima_menu()  # Retry the menu

def hakiki_bima():
    """Main menu -> Dereva Kipato -> Hakiki Bima"""
    print("\nIngiza namba ya bima (covernote)")
    print("#. Rudi nyuma")

    covernote_number = input("Ingiza namba ya bima: \n").strip()

    if covernote_number == '#':
        dereva_kipato_menu()  # Go back to the previous menu
    else:
        # Assuming you have a function to verify the covernote
        if verify_covernote(covernote_number):
            print("Bima yako imehakikiwa kwa mafanikio.")
            # You can add additional steps or menu navigation here
        else:
            print("Namba ya bima si sahihi. Tafadhali jaribu tena.")
            hakiki_bima()  # Retry the menu

def verify_covernote(covernote):
    """Function to verify the covernote number."""
    # Placeholder logic for verification
    # Replace this with actual verification logic (e.g., checking a database)
    return True if covernote else False  # Simplified for demonstration

def dereva_kipato_madai_menu():
    """Main menu -> Dereva Kipato -> Madai"""
    print("\nJe watoa taarifa kama:")
    print("1. Mwenye Bima")
    print("2. Mwakilishi wa mwenye Bima")
    print("#. Rudi nyuma")

    choice = input("Chagua chaguo: \n").strip()

    if choice == '1':
        dereva_kipato_mwenye_bima_menu()
    elif choice == '2':
        dereva_kipato_mwakilishi_bima_menu()
    elif choice == '#':
        dereva_kipato_menu()  # Go back to the main menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        dereva_kipato_madai_menu()  # Retry the menu

def dereva_kipato_mwenye_bima_menu():
    """Main menu -> Input phone number for the policyholder."""
    print("\nKwa mawasiliano taja namba ya SIMU yako ya kiganjani inayopatikana kiurahisi.")
    print("#. Rudi nyuma")

    phone_number = input("Ingiza namba ya simu: \n").strip()

    if phone_number == '#':
        dereva_kipato_madai_menu()  # Go back to the previous menu
    else:
        if validate_phone_number(phone_number):
            print(f"Madai yamewasilishwa. Utawasiliana kupitia namba hii: {phone_number}.")
            user_data["madai_mteja_phone_number"] = phone_number
            # Additional steps can be added here
        else:
            print("Namba ya simu si sahihi. Tafadhali jaribu tena.")
            dereva_kipato_mwenye_bima_menu()  # Retry the input
            
def dereva_kipato_mwakilishi_bima_menu():
    """Input phone number for the representative."""
    print("\nKwa mawasiliano taja namba ya SIMU yako ya kiganjani inayopatikana kiurahisi.")
    print("#. Rudi nyuma")

    phone_number = input("Ingiza namba ya simu: \n").strip()

    if phone_number == '#':
        dereva_kipato_madai_menu()  # Go back to the previous menu
    else:
        if validate_phone_number(phone_number):
            print(f"Madai yamewasilishwa. Utawasiliana kupitia namba hii: {phone_number}.")
            user_data["madai_mwakilishi_phone_number"] = phone_number
            # Additional steps can be added here
        else:
            print("Namba ya simu si sahihi. Tafadhali jaribu tena.")
            dereva_kipato_mwakilishi_bima_menu()  # Retry the input
            
def validate_phone_number(phone_number):
    """Validate the phone number format."""
    # Example validation: Check if it's a digit and has the correct length (10 digits)
    return phone_number.isdigit() and len(phone_number) == 10  # Adjust as needed
            
def bima_ya_safari_menu():
    """Bima ya Safari (Travel Insurance) Menu"""
    print("\nBima ya Safari(Travel Insurance) ✈️🌎🗺️🧳")
    print("1. Nunua 💵")
    print("2. Angalia Bei na Fidia 🏷️")
    print("3. Hakiki bima ✅")
    print("4. Madai ☂️")
    print("# - Kurudi menu kuu")
    print("\nKwa Huduma kwa wateja tafadhali piga namba 07# 424 205.")

    choice = input("Chagua chaguo: \n").strip()

    if choice == '1':
        nunua_bima_ya_safari_menu()
    elif choice == '2':
        angalia_bei_na_fidia()
    elif choice == '3':
        hakiki_bima_ya_safari()
    elif choice == '4':
        madai_bima_ya_safari()
    elif choice == '#':
        main_menu()  # Return to the main menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        bima_ya_safari_menu()  # Retry the menu


def nunua_bima_ya_safari_menu():
    """main menu -> Bima ya safari -> Nunua"""
    print("\nJe unasafiri kwenda")
    print("1. Mabara ya Amerika")
    print("2. Ulaya/Eneo la Schengen")
    print("3. Asia")
    print("4. Afrika")
    print("5. Eneo jingine au jumuisho lolote ya maeneo tajwa kati ya (1) hadi (4).")
    print("# - Kurudi nyuma")
    
    choice = input("Chagua chaguo: \n").strip()
    
    if choice == '1':
        mabara_ya_amerika()
    elif choice == '2':
        ulaya_schengen()
    elif choice == '3':
        asia()
    elif choice == '4':
        afrika()
    elif choice == '5':
        eneo_jingine()
    elif choice == '#':
        bima_ya_safari_menu()  # Go back to the Travel Insurance menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        nunua_bima_ya_safari_menu()  # Retry the purchase menu


def mabara_ya_amerika():
    """Main menu -> Bima ya safari -> Nunua -> Mabara ya Amerika"""
    user_data["insurance_location"] = "Mabara ya Amerika"
    
    # Input date of birth
    dob = input("Taja tarehe ya KUZALIWA ya msafiri (Siku/Mwezi/Mwaka mfano 30/07/1991): \n").strip()
    if dob == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(dob):
        print("Tarehe si sahihi. Tafadhali jaribu tena.")
        mabara_ya_amerika()  # Retry current function
        return
    user_data['DOB'] = dob

    # Input insurance start date
    insurance_start = input("Taja tarehe ya *KUANZA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_start == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_start):
        print("Tarehe ya kuanza si sahihi. Tafadhali jaribu tena.")
        mabara_ya_amerika()  # Retry current function
        return
    user_data["insurance_start_date"] = insurance_start

    # Input insurance end date
    insurance_end = input("Taja tarehe ya *KUISHA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_end == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_end):
        print("Tarehe ya kuisha si sahihi. Tafadhali jaribu tena.")
        mabara_ya_amerika()  # Retry current function
        return
    user_data["insurance_end_date"] = insurance_end
    
    # Calculate age and duration
    age = calculate_age(dob)
    duration = calculate_duration(insurance_start, insurance_end)
    
    # Summary of purchase
    print("\n*Muhtasari wa manunuzi*\n")
    print("*Bei*: TZS 151,000")
    print("*Aina ya Bima*: Mabara ya Amerika")
    print(f"*Tarehe ya kuzaliwa*: {dob}")
    print(f"*Umri*: {age} (miaka)")
    print(f"*Tarehe ya kuanza Bima*: {insurance_start}")
    print(f"*Tarehe ya kuisha Bima*: {insurance_end}")
    print(f"*Muda wa Bima*: {duration} siku")

    print("\nBofya link hapo chini kuona fidia za bima:")
    print("https://web.bimapap.co.tz/docs/benefits-americas.pdf")
    print("\nInajumuisha gharama za msafiri kutibiwa na kulazwa hospitali iwapo ameugua virusi vya Corona (COVID-19) nje ya nchi. Vigezo na masharti kuzingatiwa.\n")
    
    print("1. Endelea KUNUNUA")
    print("2. Kutoka")
    
    choice = input("Chagua chaguo: \n").strip()
    if choice == '1':
        nunua_bima_ya_safari()
    elif choice == '2':
        exit_bima()

def validate_date(date_str):
    """Helper function to validate date format as DD/MM/YYYY."""
    pattern = r'^\d{1,2}/\d{1,2}/\d{4}$'
    return re.match(pattern, date_str)

def calculate_age(dob):
    """
    Calculate the age of the user based on the date of birth.
    
    Parameters:
        dob (str): Date of birth in the format 'DD/MM/YYYY'.
    
    Returns:
        int: Age in years.
    """
    dob = datetime.strptime(dob, "%d/%m/%Y")  # Convert string to datetime object
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  # Calculate age
    return age

def calculate_duration(start, end):
    """
    Calculate the duration between the start and end date of the insurance period.
    
    Parameters:
        start (str): Start date in the format 'DD/MM/YYYY'.
        end (str): End date in the format 'DD/MM/YYYY'.
    
    Returns:
        int: Duration in days.
    """
    start_date = datetime.strptime(start, "%d/%m/%Y")  # Convert start date string to datetime object
    end_date = datetime.strptime(end, "%d/%m/%Y")  # Convert end date string to datetime object
    duration = (end_date - start_date).days  # Calculate difference in days
    return duration

def nunua_bima_ya_safari():
    """Placeholder for proceeding to purchase safari insurance."""
    print("Unanunua bima...")

def exit_bima():
    """Placeholder for exiting."""
    print("Asante kwa kutumia BimaChap!")
    exit()

def ulaya_schengen():
    """Main menu -> Bima ya safari -> Nunua -> Ulaya/Eneo la Schengen"""
    user_data["insurance_location"] = "Ulaya/Eneo la Schengen"
    
    # Input date of birth
    dob = input("Taja tarehe ya KUZALIWA ya msafiri (Siku/Mwezi/Mwaka mfano 30/07/1991): \n").strip()
    if dob == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(dob):
        print("Tarehe si sahihi. Tafadhali jaribu tena.")
        ulaya_schengen()  # Retry current function
        return
    user_data['DOB'] = dob

    # Input insurance start date
    insurance_start = input("Taja tarehe ya *KUANZA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_start == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_start):
        print("Tarehe ya kuanza si sahihi. Tafadhali jaribu tena.")
        ulaya_schengen()  # Retry current function
        return
    user_data["insurance_start_date"] = insurance_start

    # Input insurance end date
    insurance_end = input("Taja tarehe ya *KUISHA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_end == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_end):
        print("Tarehe ya kuisha si sahihi. Tafadhali jaribu tena.")
        ulaya_schengen()  # Retry current function
        return
    user_data["insurance_end_date"] = insurance_end
    
    # Calculate age and duration
    age = calculate_age(dob)
    duration = calculate_duration(insurance_start, insurance_end)
    
    # Summary of purchase
    print("\n*Muhtasari wa manunuzi*\n")
    print("*Bei*: TZS 151,000")
    print("*Aina ya Bima*: Ulaya/Eneo la Schengen")
    print(f"*Tarehe ya kuzaliwa*: {dob}")
    print(f"*Umri*: {age} (miaka)")
    print(f"*Tarehe ya kuanza Bima*: {insurance_start}")
    print(f"*Tarehe ya kuisha Bima*: {insurance_end}")
    print(f"*Muda wa Bima*: {duration} siku")

    print("\nBofya link hapo chini kuona fidia za bima:")
    print("https://web.bimapap.co.tz/docs/benefits-schengen.pdf")
    print("\nInajumuisha gharama za msafiri kutibiwa na kulazwa hospitali iwapo ameugua virusi vya Corona (COVID-19) nje ya nchi. Vigezo na masharti kuzingatiwa.\n")
    
    print("1. Endelea KUNUNUA")
    print("2. Kutoka")
    
    choice = input("Chagua chaguo: \n").strip()
    if choice == '1':
        nunua_bima_ya_safari()
    elif choice == '2':
        exit_bima()
def asia():
    """Main menu -> Bima ya safari -> Nunua -> Asia"""
    user_data["insurance_location"] = "Asia"
    
    # Input date of birth
    dob = input("Taja tarehe ya KUZALIWA ya msafiri (Siku/Mwezi/Mwaka mfano 30/07/1991): \n").strip()
    if dob == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(dob):
        print("Tarehe si sahihi. Tafadhali jaribu tena.")
        asia()  # Retry current function
        return
    user_data['DOB'] = dob

    # Input insurance start date
    insurance_start = input("Taja tarehe ya *KUANZA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_start == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_start):
        print("Tarehe ya kuanza si sahihi. Tafadhali jaribu tena.")
        asia()  # Retry current function
        return
    user_data["insurance_start_date"] = insurance_start

    # Input insurance end date
    insurance_end = input("Taja tarehe ya *KUISHA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_end == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_end):
        print("Tarehe ya kuisha si sahihi. Tafadhali jaribu tena.")
        asia()  # Retry current function
        return
    user_data["insurance_end_date"] = insurance_end
    
    # Calculate age and duration
    age = calculate_age(dob)
    duration = calculate_duration(insurance_start, insurance_end)
    
    # Summary of purchase
    print("\n*Muhtasari wa manunuzi*\n")
    print("*Bei*: TZS 151,000")
    print("*Aina ya Bima*: Asia")
    print(f"*Tarehe ya kuzaliwa*: {dob}")
    print(f"*Umri*: {age} (miaka)")
    print(f"*Tarehe ya kuanza Bima*: {insurance_start}")
    print(f"*Tarehe ya kuisha Bima*: {insurance_end}")
    print(f"*Muda wa Bima*: {duration} siku")

    print("\nBofya link hapo chini kuona fidia za bima:")
    print("https://web.bimapap.co.tz/docs/benefits-asia.pdf")
    print("\nInajumuisha gharama za msafiri kutibiwa na kulazwa hospitali iwapo ameugua virusi vya Corona (COVID-19) nje ya nchi. Vigezo na masharti kuzingatiwa.\n")
    
    print("1. Endelea KUNUNUA")
    print("2. Kutoka")
    
    choice = input("Chagua chaguo: \n").strip()
    if choice == '1':
        nunua_bima_ya_safari()
    elif choice == '2':
        exit_bima()


def afrika():
    """Main menu -> Bima ya safari -> Nunua -> Afrika"""
    user_data["insurance_location"] = "Afrika"
    
    # Input date of birth
    dob = input("Taja tarehe ya KUZALIWA ya msafiri (Siku/Mwezi/Mwaka mfano 30/07/1991): \n").strip()
    if dob == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(dob):
        print("Tarehe si sahihi. Tafadhali jaribu tena.")
        afrika()  # Retry current function
        return
    user_data['DOB'] = dob

    # Input insurance start date
    insurance_start = input("Taja tarehe ya *KUANZA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_start == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_start):
        print("Tarehe ya kuanza si sahihi. Tafadhali jaribu tena.")
        afrika()  # Retry current function
        return
    user_data["insurance_start_date"] = insurance_start

    # Input insurance end date
    insurance_end = input("Taja tarehe ya *KUISHA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_end == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_end):
        print("Tarehe ya kuisha si sahihi. Tafadhali jaribu tena.")
        afrika()  # Retry current function
        return
    user_data["insurance_end_date"] = insurance_end
    
    # Calculate age and duration
    age = calculate_age(dob)
    duration = calculate_duration(insurance_start, insurance_end)
    
    # Summary of purchase
    print("\n*Muhtasari wa manunuzi*\n")
    print("*Bei*: TZS 151,000")
    print("*Aina ya Bima*: Africa Only")
    print(f"*Tarehe ya kuzaliwa*: {dob}")
    print(f"*Umri*: {age} (miaka)")
    print(f"*Tarehe ya kuanza Bima*: {insurance_start}")
    print(f"*Tarehe ya kuisha Bima*: {insurance_end}")
    print(f"*Muda wa Bima*: {duration} siku")

    print("\nBofya link hapo chini kuona fidia za bima:")
    print("https://web.bimapap.co.tz/docs/benefits-africa.pdf")
    print("\nInajumuisha gharama za msafiri kutibiwa na kulazwa hospitali iwapo ameugua virusi vya Corona (COVID-19) nje ya nchi. Vigezo na masharti kuzingatiwa.\n")
    
    print("1. Endelea KUNUNUA")
    print("2. Kutoka")
    
    choice = input("Chagua chaguo: \n").strip()
    if choice == '1':
        nunua_bima_ya_safari()
    elif choice == '2':
        exit_bima()

def eneo_jingine():
    """Main menu -> Bima ya safari -> Nunua -> Eneo jingine"""
    user_data["insurance_location"] = "Eneo jingine"
    
    # Input date of birth
    dob = input("Taja tarehe ya KUZALIWA ya msafiri (Siku/Mwezi/Mwaka mfano 30/07/1991): \n").strip()
    if dob == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(dob):
        print("Tarehe si sahihi. Tafadhali jaribu tena.")
        eneo_jingine()  # Retry current function
        return
    user_data['DOB'] = dob

    # Input insurance start date
    insurance_start = input("Taja tarehe ya *KUANZA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_start == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_start):
        print("Tarehe ya kuanza si sahihi. Tafadhali jaribu tena.")
        eneo_jingine()  # Retry current function
        return
    user_data["insurance_start_date"] = insurance_start

    # Input insurance end date
    insurance_end = input("Taja tarehe ya *KUISHA* kwa bima (Siku/Mwezi/Mwaka mfano 30/07/2021): \n").strip()
    if insurance_end == "#":
        nunua_bima_ya_safari_menu()  # Go back if user inputs #
        return
    if not validate_date(insurance_end):
        print("Tarehe ya kuisha si sahihi. Tafadhali jaribu tena.")
        eneo_jingine()  # Retry current function
        return
    user_data["insurance_end_date"] = insurance_end
    
    # Calculate age and duration
    age = calculate_age(dob)
    duration = calculate_duration(insurance_start, insurance_end)

    # Summary of purchase
    print("\n*Muhtasari wa manunuzi*\n")
    print("*Bei*: TZS 151,000")
    print("*Aina ya Bima*: Africa Only")
    print(f"*Tarehe ya kuzaliwa*: {dob}")
    print(f"*Umri*: {age} (miaka)")
    print(f"*Tarehe ya kuanza Bima*: {insurance_start}")
    print(f"*Tarehe ya kuisha Bima*: {insurance_end}")
    print(f"*Muda wa Bima*: {duration} siku")

    print("\nBofya link hapo chini kuona fidia za bima:")
    print("https://web.bimapap.co.tz/docs/benefits-africa.pdf")
    print("\nInajumuisha gharama za msafiri kutibiwa na kulazwa hospitali iwapo ameugua virusi vya Corona (COVID-19) nje ya nchi. Vigezo na masharti kuzingatiwa.\n")
    
    print("1. Endelea KUNUNUA")
    print("2. Kutoka")
    
    choice = input("Chagua chaguo: \n").strip()
    if choice == '1':
        nunua_bima_ya_safari()
    elif choice == '2':
        exit_bima()

def angalia_bei_na_fidia():
    """take the user to the nunua bima ya safari flow"""
    nunua_bima_ya_safari_menu()

def hakiki_bima_ya_safari():
    hakiki_bima()

def madai_bima_ya_safari():
    """Main menu -> Bima ya safari -> Madai"""
    print("Madai ☂️")
    print("Tafadhali wasilisha madai yako kwa travel@insurance.com.")
    print("Taarifa muhimu: Jina lako, Namba ya Pasipoti na Maelezo ya awali ya madai ya Bima.")
    print("Asante kwa kutumia BimaChap!")

    print("\nTuma # kurudi Menu Bima ya Safari")
    choice = input("Chagua chaguo: \n").strip()
    if choice == "#":
        nunua_bima_ya_safari_menu()  # Go back to the main insurance menu


def vigezo_na_masharti_menu():
    """Menu for Terms and Conditions"""
    print("Vigezo na Masharti")
    print("Kusoma taratibu, vigezo na masharti ya:")
    print("1. Bima ndogo (third party)")
    print("2. Safari (Travel)")
    print("3. Bima ya Ajali (Dereva)")
    print("# - Kurudi nyuma")  # Option to go back

    choice = input("Chagua chaguo: \n").strip()
    if choice == '1':
        print("You selected Bima ndogo (third party).")  # Placeholder for further actions
        # Call the function related to Bima ndogo if implemented
    elif choice == '2':
        print("You selected Safari (Travel).")  # Placeholder for further actions
        # Call the function related to Safari (Travel) if implemented
    elif choice == '3':
        print("You selected Bima ya Ajali (Dereva).")  # Placeholder for further actions
        # Call the function related to Bima ya Ajali if implemented
    elif choice == '#':
        nunua_bima_ya_safari()  # Assuming this function exists to go back to the main insurance menu
    else:
        print("Chaguo si sahihi. Tafadhali jaribu tena.")
        vigezo_na_masharti_menu()  # Re-display the menu for valid input

    # Prompting the user to press # to return or exit
    print("\nBonyeza # kurudi kwenye menyu kuu, au chochote kingine kuondoka.")
    final_choice = input("Chaguo lako: \n").strip()
    if final_choice == '#':
        nunua_bima_ya_safari()  # Return to the main menu
    else:
        print("Asante kwa kutumia BimaChap!")  # Thank the user and exit


def ofisi_zetu_menu():
    print("You selected Ofisi zetu (Our offices)")

# Call the main menu to start the chatbot
main_menu()
