import datetime

from sw.database import DB


class Films(object):
    COLLECTION = "films"

    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        if not DB.find_one(self.COLLECTION, {"episode_id": self.episode_id}):
            DB.insert(collection=self.COLLECTION, data=self.json())

    def json(self):
        return {
            'title': self.title,
            'episode_id': self.episode_id,
            'opening_crawl': self.opening_crawl,
            'director': self.director,
            'producer': self.producer,
            'release_date': self.release_date,
            'created_at': self.created_at
        }
