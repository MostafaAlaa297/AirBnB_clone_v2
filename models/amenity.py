#!/usr/bin/python3
"""
===========
Amenity module.
===========
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class."""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
