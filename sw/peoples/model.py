import datetime

from sw.database import DB


class Peoples(object):
    COLLECTION = "peoples"

    def __init__(self, name, height, mass, hair_color, skin_color, gender):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.gender = gender
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        if not DB.find_one(self.COLLECTION, {"name": self.name}):
            DB.insert(collection=self.COLLECTION, data=self.json())

    def json(self):
        return {
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'gender': self.gender,
            'created_at': self.created_at
        }
