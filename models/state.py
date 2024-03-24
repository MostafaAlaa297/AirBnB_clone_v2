#!/usr/bin/python3
"""
============
State module
============
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.filestorage import storage
from models import City


class State(BaseModel, Base):
    """State class"""
    cities = relationship("City", backref="state", cascade="all, delete")
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Returns the list of city instances 
        with state_id equals to current State.id"""
        city_object = storage.all(City)
        return [city for city in city_object.values() if city.state_id == self.id]
