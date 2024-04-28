#!/usr/bin/python3
"""
============
State module
============
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class"""
    if models.storage_type == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)

<<<<<<< HEAD
    @property
    def cities(self):
        from models import City
        """Returns the list of city instances 
        with state_id equals to current State.id"""
        city_object = storage.all(City)
        return [city for city in city_object.values() if city.state_id == self.id]
=======
    if models.storage_type != "db":
        @property
        def cities(self):
            from models import City
            """Returns the list of city instances 
            with state_id equals to current State.id"""
            city_object = storage.all(City)
            return [city for city in city_object.values() if city.state_id == self.id]
>>>>>>> df59e28227de2a313273f50a8ddfe2c0dd3c1c0c
