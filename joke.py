import requests
from bs4 import BeautifulSoup as bs


def get_requests(url):
    # We get a joke
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    return soup.find_all('div', class_='tecst')


class Joke:

    def __init__(self):
        self.jokes = []
        self.links = ["https://anekdotbar.ru"]
        self.get_link()
        self.get_joke()
        self.number_of_jokes = len(self.jokes)
        print(f'Количество шуток: {self.number_of_jokes}')

    def get_link(self):
        for i in range(10):
            self.links.append(f"https://anekdotbar.ru/page/{i + 2}/")

    def get_joke(self):
        try:
            for link in self.links:
                for i in get_requests(link):
                    self.jokes.append(i.text)
        except requests.exceptions.ConnectionError as e:
            print(f"Сайт недоступен")
