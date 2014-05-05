# Copyright (c) 2014 Adam Coldrick (SotK)

import yaml

import coldtealib

class Database():

    """Class to handle the database of books."""

    def __init__(self, data):
        """Initialise the database."""
        self.data = data

    @class_method
    def from_file(cls, path):
        data = yaml.load(path)
        return Database(data)
