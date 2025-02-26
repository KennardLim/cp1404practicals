"""
Wimbledon
Estimate: 60 minutes / 1 hour
Actual: 55 minutes
"""

def main():
    """Read the record files, and then processes the data to display
        the champions and their win count, afterward displays the countries who have won
        in alphabetical order."""
    wimbledon_records = read_file_into_data("wimbledon.csv")
    champion_to_wins = count_champion_wins(wimbledon_records)
    winning_countries = ", ".join(get_winning_countries(wimbledon_records))
    print("Wimbledon Champions:")
    for champion, number_of_wins in champion_to_wins.items():
        print(champion, number_of_wins)
    print()
    print(f"These {len(winning_countries)} have won Wimbledon: ")
    print(winning_countries)

def read_file_into_data(filename):
    """Read the record files and processes each line into a data list of the records"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        file_data = in_file.readlines()
        file_data.pop(0)
        data = [line.strip().split(",") for line in file_data]
    return data

def count_champion_wins(records):
    """Stores each champion and how many times they have won into a dictionary"""
    champion_to_wins = dict()
    for data in records:
        if data[2] in champion_to_wins:
            champion_to_wins[data[2]] += 1
        else:
            champion_to_wins[data[2]] = 1
    return champion_to_wins

def get_winning_countries(records):
    """Records each country that has had a winning champion and sorts them in alphabetical order"""
    winning_countries = set()
    for data in records:
        winning_countries.add(data[1])
    return sorted(winning_countries)

main()