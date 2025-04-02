from ast import Index

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Simulates a taxi service, you can choose a taxi and drive it your chosen distance,
    the fare will be added to your total bill each time you drive a taxi."""
    current_taxi = None
    total_bill = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(TAXIS)
            current_taxi = choose_taxi(TAXIS)
        elif choice == "d":
            total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:,.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:,.2f}")
    print("Taxis are now:")
    display_taxis(TAXIS)

def display_taxis(taxis):
    """Display all the available taxis alongside their index number."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Gets the taxi based on its index number."""
    taxi_choice = int(input("Choose taxi: "))
    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")

def drive_taxi(taxi):
    """Drive a taxi a chosen distance and gives you back the fare."""
    try:
        taxi.start_fare()
        drive_distance = int(input("Drive how far? "))
        taxi.drive(drive_distance)
        print(f"Your {taxi.name} trip cost you {taxi.get_fare():,.2f}")
        return taxi.get_fare()
    except AttributeError:
        print("You need to choose a taxi before you can drive")
        return 0

main()