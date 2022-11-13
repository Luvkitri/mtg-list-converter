import csv
import os
import re

from datetime import datetime


def main():
    source_directory_path = "./mtg-collection"

    cards = []
    for filename in os.listdir(source_directory_path):
        with open(os.path.join(source_directory_path, filename), "r") as source_file:
            for line in source_file.readlines():
                result = re.search(r"^(\d+)([^\(]+) \((.*?)\) (\d+)(.*)", line)

                groups = result.groups()

                cards.append(
                    {
                        "card_name": groups[1].strip(),
                        "amount": groups[0],
                        "set_name": groups[2].upper(),
                        "collector_number": groups[3],
                        "is_foil": "1" if groups[4] != "" else "0",
                    }
                )
                

    with open(f"card-list-{datetime.now()}.csv", mode="w+", newline="") as output_file:
        fieldnames = ["card_name", "amount", "set_name", "collector_number", "is_foil"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(cards)


if __name__ == "__main__":
    main()
