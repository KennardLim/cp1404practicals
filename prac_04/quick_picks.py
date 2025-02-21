import random

quick_picks = []
NUMBERS_PER_QUICK_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    """Ask the user for how many quick picks to generate before displaying the inputted amount of quick picks"""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_picks.append(generate_quick_pick(MINIMUM_NUMBER, MAXIMUM_NUMBER, NUMBERS_PER_QUICK_PICK))
    for quick_pick in quick_picks:
        print(" ".join([f"{number:2}" for number in quick_pick]))

def generate_quick_pick(minimum, maximum, length):
    """Generate a list of numbers in ascending order without duplicate numbers"""
    quick_pick = []
    while len(quick_pick) != length:
        random_number = random.randint(1,45)
        if random_number not in quick_pick:
            quick_pick.append(random_number)
    return sorted(quick_pick)

main()


