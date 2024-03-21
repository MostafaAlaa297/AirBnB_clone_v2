#!/usr/bin/python3
"""
===========
State module.
===========
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class."""
    cities = relationship("City", backref="state", cascade="all, delete")
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        self.cities
