from guitar import Guitar

def main():
    guitars = read_file_into_guitars("guitars.csv")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def read_file_into_guitars(filename):
    """Read the csv file and processes each line into a guitar and puts it into a guitar list"""
    guitars = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            guitar_parts = line.strip("\n").split(",")
            guitar = Guitar(guitar_parts[0], int(guitar_parts[1]), float(guitar_parts[2]))
            guitars.append(guitar)
    return guitars

main()
