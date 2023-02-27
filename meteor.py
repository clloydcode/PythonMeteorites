import csv
import re


class Meteor:
    all = []

    def __init__(self, meteor_name, meteor_id, meteor_class, meteor_mass, meteor_year, geo_loc):

        self.__meteor_name = self.__parse_meteor_name(meteor_name)
        self.__meteor_id = meteor_id
        self.__meteor_class = meteor_class
        self.__meteor_mass = meteor_mass
        self.__meteor_year = self.__parse_meteor_year(meteor_year)
        self.__geo_loc = self.__parse_geo_loc(geo_loc)

        Meteor.all.append(self)

    @property
    def meteor_name(self):
        return self.__meteor_name

    @property
    def meteor_id(self):
        return self.__meteor_id

    @property
    def meteor_class(self):
        return self.__meteor_class

    @property
    def meteor_mass(self):
        return self.__meteor_mass

    @property
    def meteor_year(self):
        return self.__meteor_year

    @property
    def geo_loc(self):
        return self.__geo_loc

    @staticmethod
    def __parse_geo_loc(value):
        if len(value) < 1:
            return "0.0, 0.0"
        else:
            # removes all non-alpha and non-numeric chars except space , . -
            return re.sub('[^A-Za-z0-9,. -]+', '', value)

    @staticmethod
    def __parse_meteor_year(value):
        if len(str(value)) != 4:
            return "????"
        else:
            return value

    @staticmethod
    def __parse_meteor_name(value):
        if len(value) < 1:
            return "Unknown"
        else:
            return value

    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            meteors = list(reader)

        for meteor in meteors:
            Meteor(
                meteor_name=meteor.get('name'),
                meteor_id=meteor.get('id'),
                meteor_class=meteor.get('recclass'),
                meteor_year=meteor.get('year'),
                meteor_mass=meteor.get('mass (g)'),
                geo_loc=meteor.get('GeoLocation'),
            )

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__meteor_name}', {self.__meteor_id}, '{self.__meteor_class}', " \
               f"'{self.__meteor_year}', '{self.__meteor_mass}', '{self.__geo_loc}')"
