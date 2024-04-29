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
from models.city import City

class State(BaseModel, Base):
    """State class"""

    if models.storage_type == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
    else:
        print("we are here fs")
        name = ""

        def __init__(self, *args, **kwargs):
            """Initializes state"""
            super().__init__(*args, **kwargs)

        @property
        def cities(self):
            """Returns the list of city instances 
            with state_id equals to current State.id"""
            citiesList = []
            citiesAll = storage.all(City)
            for city in citiesAll.values():
                if city.state_id == self.id:
                    citiesList.append(city)
            return citiesList
            #city_object = storage.all(City)
            #return [city for city in city_object.values() if city.state_id == self.id]
