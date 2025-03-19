"""
Guitars!
Estimate: 50 minutes
Actual: 55 minutes
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("\nName: ")
print("\n... snip ...\n")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

maximum_name_length = len(max([guitar.name for guitar in guitars], key=len))
maximum_price_length = len(max([f"{guitar.cost:10,.2f}" for guitar in guitars], key=len))

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{maximum_name_length}} ({guitar.year}), worth ${guitar.cost:{maximum_price_length},.2f} {vintage_string}")
