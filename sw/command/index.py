import click
import requests
from sw.films.model import Films
from sw.peoples.model import Peoples


@click.command()
def create_data():
    create_films()
    create_peoples()


def create_films():
    r = requests.get('https://swapi.co/api/films')

    data = r.json()

    for film in data['results']:
        film = Films(film['title'],
                     film['episode_id'],
                     film['opening_crawl'],
                     film['director'],
                     film['producer'],
                     film['release_date'])
        film.insert()


def create_peoples(url: str = "https://swapi.co/api/people"):
    r = requests.get(url)

    data = r.json()

    for people in data['results']:
        people = Peoples(people['name'],
                         people['height'],
                         people['mass'],
                         people['hair_color'],
                         people['skin_color'],
                         people['gender'])
        people.insert()

    while data['next'] is not None:
        return create_peoples(data['next'])
