#!/usr/bin/python3
"""
==================
FileStorage module
==================
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File Storage class"""
    __file_path = "file.json"
    __objects = {
    }

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        cls_dict = {}
        for key, obj in FileStorage.__objects.items():
            if cls is None:
                return FileStorage.__objects
            elif key.split('.')[0] == cls.__name__:
                cls_dict[key] = str(obj)
        
        return cls_dict
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj_attrs in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    obj = cls(**obj_attrs)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object"""
        if not obj:
            pass
        for key, val in FileStorage.__objects.items():
            if val == obj:
                FileStorage.__objects.pop(key)

    def close(self):
        """deserializes the obj"""
        self.reload()
