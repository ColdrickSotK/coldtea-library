# Copyright (c) 2014 Adam Coldrick (SotK)

import yaml

import coldtealib

class Database():

    """Class to handle the database of books."""

    def __init__(self, data):
        """Initialise the database."""
        self.data = data

    def __repr__(self):
        """Return a nice representation of the database."""
        return yaml.dump(self.data, default_flow_style=False)

    def __str__(self):
        return self.__repr__()

    @classmethod
    def from_file(cls, handle):
        """Load the database from a file, return the loaded database.

        Takes an open file handle and loads the contents as YAML.

        """
        data = yaml.load(handle)
        return Database(data)

    def to_file(self, handle):
        """Save the database to a file in YAML format."""
        handle.write(self.__repr__())
