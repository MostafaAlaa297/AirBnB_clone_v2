#!/usr/bin/python3
"""
============
State module
============
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    cities = relationship("City", backref="state", cascade="all, delete")
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type != "db":
    	@property
    	def cities(self):
        	from models import City
        	"""Returns the list of city instances 
        	with state_id equals to current State.id"""
        	city_object = storage.all(City)
        	return [city for city in city_object.values() if city.state_id == self.id]
