#!/usr/bin/python3
"""
===========
City module.
===========
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column


class City(BaseModel, Base):
    """City class."""
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
