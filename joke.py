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
        self.links = ["https://anekdotbar.ru", "https://anekdotbar.ru/page/2/", "https://anekdotbar.ru/page/3/", " https://anekdotbar.ru/page/4/", "https://anekdotbar.ru/page/5/", "https://anekdotbar.ru/page/6/", "https://anekdotbar.ru/page/7/", "https://anekdotbar.ru/page/8/", "https://anekdotbar.ru/page/9/", "https://anekdotbar.ru/page/10/"]
        self.get_joke()
        self.number_of_jokes = len(self.jokes)
        print(self.number_of_jokes)

    def get_joke(self):
        try:
            for link in self.links:
                for i in get_requests(link):
                    self.jokes.append(i.text)
        except requests.exceptions.ConnectionError as e:
            print(f"Сайт недоступен: {e}")

