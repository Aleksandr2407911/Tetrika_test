import requests
from bs4 import BeautifulSoup
import csv
import string


class AnimalCounter:
    def __init__(self):
        self.base_url = "https://ru.wikipedia.org"
        self.start_url = f"{self.base_url}/wiki/Категория:Животные_по_алфавиту"
        self.animals_count = {letter: 0 for letter in string.ascii_uppercase}

    def get_animals_count(self) -> dict:
        url = self.start_url

        while url:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            category_groups = soup.find_all("div", class_="mw-category-group")
            for group in category_groups:
                header = group.find("h3").text.strip()
                if header and header[0].upper() in self.animals_count:
                    count = len(group.find_all("a"))
                    self.animals_count[header[0].upper()] += count

            next_page = soup.find("a", string="Следующая страница")
            if next_page:
                url = self.base_url + next_page["href"]
            else:
                url = None

        return self.animals_count

    def write_to_csv(self, data: dict, file_path: str = "./task2/beasts.csv") -> None:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for letter, count in sorted(data.items()):
                writer.writerow([letter, count])

    def __call__(self) -> None:
        animals = self.get_animals_count()
        self.write_to_csv(animals)


if __name__ == "__main__":
    AnimalCounter()()
