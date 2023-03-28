#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel
from models.base_model import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, base):
    """ State class """

    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)
    cities = relationship(
        "City", cascade="all, delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage

            new_list = []

            for city_object, value in storage.all(City).items():
                if self.id == value.state_id:
                    new_list.append(value)
            return new_list
