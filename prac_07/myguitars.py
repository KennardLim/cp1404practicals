from guitar import Guitar

GUITAR_DATA_FILE = "guitars.csv"

def main():
    """Gets a list of guitar from a csv file,
    then asks the user for any more guitars to add,
    afterward displays the list of guitars before
    writing the new list back into the csv file"""
    print(f"Fetching guitars from {GUITAR_DATA_FILE}...")
    guitars = read_file_into_guitars(GUITAR_DATA_FILE)
    print("\n... snip ...\n")
    print(f"My guitars from {GUITAR_DATA_FILE} fetched!")

    # guitars.append(Guitar("Ol Reliable", 1864, 16035.40)) # debugging
    # guitars.append(Guitar("N3w R3tr0 790z", 2025, 1512.9)) # debugging

    print("Add some more guitars, enter a blank name to finalize.")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("\nName: ")
    print("\n... snip ...\n")

    guitars.sort()
    print("These are my guitars:")
    display_guitars(guitars)

    print(f"Saving guitars to {GUITAR_DATA_FILE}...")
    print("\n... snip ...\n")
    write_guitars_into_file(GUITAR_DATA_FILE, guitars)
    print(f"Guitars saved to {GUITAR_DATA_FILE}!")

def read_file_into_guitars(filename):
    """Read the csv file and processes each line into a guitar and puts it into a guitar list"""
    guitars = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            guitar_parts = line.strip("\n").split(",")
            guitar = Guitar(guitar_parts[0], int(guitar_parts[1]), float(guitar_parts[2]))
            guitars.append(guitar)
    return guitars

def write_guitars_into_file(filename, guitars):
    """Write the list of guitar objects into a csv file"""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            guitar_line = f"{guitar.name},{guitar.year},{guitar.cost}\n"
            out_file.write(guitar_line)

def display_guitars(guitars):
    """Display the guitars into a readable list along with the guitar's data"""
    maximum_number_length = len(str(len(guitars)))
    maximum_name_length = len(max([guitar.name for guitar in guitars], key=len))
    maximum_price_length = len(max([f"{guitar.cost:10,.2f}" for guitar in guitars], key=len))
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i:<{maximum_number_length}}: {guitar.name:>{maximum_name_length}} ({guitar.year}), "
              f"worth ${guitar.cost:{maximum_price_length},.2f} {vintage_string}")

main()
