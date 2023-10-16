import random
import requests
from bs4 import BeautifulSoup

URL = 'https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0' \
      '%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb'


def main():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())
    trs = soup.select("table tr")
    place, film_name, year, director, film_genre = [], [], [], [], []

    for elem in trs[1:]:
        td_elems = elem.findAll('td')
        # print(td_elems[0].text, td_elems[1].text, td_elems[2].text, td_elems[3].text, td_elems[4].text)
        place.append(td_elems[0].text)
        film_name.append(td_elems[1].text)
        year.append(td_elems[2].text)
        director.append(td_elems[3].text)
        film_genre.append(td_elems[4].text)

    # for i in range(len(place)):
    #     print(place[i], film_name[i], year[i], director[i], film_genre[i])

    n_movies = len(place)

    while (True):
        idx = random.randrange(0, n_movies)

        print(
            f'#{place[idx]} - {film_name[idx]}, {year[idx]} года, Режиссер: {director[idx]}, жанры: {film_genre[idx]}')

        # comment the next line out to test user input with docker run -t -i
        # break

        user_input = input('Do you want another movie ([y]/n)? ')
        if user_input == 'n':
            break


if __name__ == '__main__':
    main()
