"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the inputted value is a string or a float point number.
2. When will a ZeroDivisionError occur?
    When the denominator input is a 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes by adding a loop to the program to reprompt the user for a denominator that isn't zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
