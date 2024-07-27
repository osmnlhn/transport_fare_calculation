from ui import display_station_board, get_user_input, display_voucher, display_menu
from logic import calculate_fare, calculate_total_zones
from datetime import datetime

def main():
    while True:
        display_station_board()
        
        start_zone = get_user_input("Enter start zone (1 for Central, 2 for Midtown, etc.): ")
        end_zone = get_user_input("Enter destination zone (1 for Central, 2 for Midtown, etc.): ")
        
        adult_count = get_user_input("Enter number of adult travellers: ")
        child_count = get_user_input("Enter number of child travellers: ")
        senior_count = get_user_input("Enter number of senior travellers: ")
        student_count = get_user_input("Enter number of student travellers: ")

        total_zones = calculate_total_zones(start_zone, end_zone)
        fares = calculate_fare(total_zones, adult_count, child_count, senior_count, student_count)
        
        voucher = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "start_zone": start_zone,
            "end_zone": end_zone,
            "total_zones": total_zones,
            "travellers": {
                "adults": adult_count,
                "children": child_count,
                "seniors": senior_count,
                "students": student_count,
            },
            "fares": fares,
        }
        
        display_voucher(voucher)
        
        if display_menu() == "end":
            break

if __name__ == "__main__":
    main()
