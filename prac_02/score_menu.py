MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    choice = input("Choice: ").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score()
            print(f"Stored {score} as your score.")
        elif choice == "p":
            result = determine_result(score)
            print(f"Your score's result is {result}.")
        elif choice == "s":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").lower()
    print("Thank you and goodnight.")

def get_valid_score():
    score = int(input("Input a valis score (between 0 and 100): "))
    while score < 0 or score > 100:
        print("Invalid score, must be between 0 and 100")
        score = int(input("Input a valid score (between 0 and 100): "))
    return score

def determine_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()