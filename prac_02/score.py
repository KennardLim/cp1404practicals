import random

def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    result = determine_result(random.randint(1, 100))
    print(result)

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