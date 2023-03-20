#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, base):
    """Amenity class"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place",
                                   secondary="place_amenity", viewonly=False)
