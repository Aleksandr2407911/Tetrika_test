import requests
from bs4 import BeautifulSoup
import csv
import string


def get_animals_count() -> dict:
    base_url = "https://ru.wikipedia.org"
    url = f"{base_url}/wiki/Категория:Животные_по_алфавиту"
    animals_count = {letter: 0 for letter in string.ascii_uppercase}

    while url:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        category_groups = soup.find_all("div", class_="mw-category-group")
        for group in category_groups:
            header = group.find("h3").text.strip()
            if header and header[0].upper() in animals_count:
                count = len(group.find_all("a"))
                animals_count[header[0].upper()] += count

        next_page = soup.find("a", string="Следующая страница")
        if next_page:
            url = base_url + next_page["href"]
        else:
            url = None

    return animals_count


def write_to_csv(data) -> None:
    with open("./task2/beasts.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for letter, count in sorted(data.items()):
            writer.writerow([letter, count])


if __name__ == "__main__":
    animals_data = get_animals_count()
    write_to_csv(animals_data)
