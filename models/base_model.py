#!/usr/bin/env python3
"""
===========
Base module
===========
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    The base class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of the base module
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Returns info about the model
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the time
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
    """
    def to_dict(self):
        
        Returns a dictionary containing all keys/values of __dict__
        
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
        """
