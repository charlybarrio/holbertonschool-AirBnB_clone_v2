#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, base
from models.review import Review
from os import getenv
from models.amenity import Amenity


place_amenity = Table('place_amenity', base.metadata,
                      Column('place_id', String(60), ForeignKey("places.id"), onupdate='CASCADE',
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey("amenities.id"), onupdate='CASCADE',
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenity_ids = []

    if getenv("HBNB_ENV") == "db":
        reviews = relationship(
            "Review", cascade="all, delete", backref="places")
        amenities = relationship(
            "Amenity", secondary="place_amenity", viewonly=False)

    @property
    def reviews(self):
        """getter for reviews for places"""

        from models import storage

        new_dict = []
        for review_object in storage.all(Review).items():
            if self.id == review_object.place_id:
                new_dict.append(review_object)
        return new_dict

    @property
    def amenities(self):
        """getter for ammenities"""

        from models import storage

        new_dict = []

        amenities = storage.all(Amenity).values()

        for amenity in amenities:
            if amenity.id in self.amenity_ids:
                new_dict.append(amenity)
        return new_dict

    @amenities.setter
    def amenities(self, ammenity):
        """setter for ammenities"""
        if type(self) == Amenity:
            self.amenity_ids.append(ammenity.id)
