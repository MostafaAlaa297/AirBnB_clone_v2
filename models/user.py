#!/usr/bin/env python3
"""
===========
User model
===========
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """User class that inherits from BaseModel."""
    __tablename__ = 'users'
 
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
