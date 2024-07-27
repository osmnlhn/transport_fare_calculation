def display_station_board():
    print("Stations Board:")
    print("Central Zone: Centrala, Yaen, Rede, Jaund, Tallan, Ninia")
    print("Midtown Zone: Quthei, Wicyt, Riladia, Oloadus, Sylas")
    print("Downtown Zone: Zord, Perinad, Keivia, Erean, Brundad")
    print("East Side Zone: Agralle, Docia, Stonyam, Ryall, Marend, Pryn")
    print("South Side Zone: Adohad, Elyot, Holmer, Vertwall, Ruril")

def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def display_voucher(voucher):
    print("\nTravel Voucher")
    print(f"Date: {voucher['date']}")
    print(f"Boarding Zone: {voucher['start_zone']}")
    print(f"Destination Zone: {voucher['end_zone']}")
    print(f"Total Zones Traveled: {voucher['total_zones']}\n")
    
    travellers = voucher["travellers"]
    fares = voucher["fares"]
    print("Traveller Details:")
    print(f"Adults: {travellers['adults']} - Fare: {fares['adults']} CENTS")
    print(f"Children: {travellers['children']} - Fare: {fares['children']} CENTS")
    print(f"Seniors: {travellers['seniors']} - Fare: {fares['seniors']} CENTS")
    print(f"Students: {travellers['students']} - Fare: {fares['students']} CENTS\n")
    
    total_travellers = sum(travellers.values())
    total_fare = sum(fares.values())
    print(f"Total Travellers: {total_travellers}")
    print(f"Total Fare: {total_fare} CENTS\n")

def display_menu():
    while True:
        choice = input("Do you want to issue another voucher or end the program? (issue/end): ").strip().lower()
        if choice in ["issue", "end"]:
            return choice
        print("Invalid input. Please enter 'issue' or 'end'.")
