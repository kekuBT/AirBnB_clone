#!/usr/bin/python3

import uuid
from datetime import datetime
# This imports the variable storage
import models


class BaseModel():
    """" defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Constructor and re-create an instance with
        this dictionary representation"""
        if len(kwargs) > 0:
            # each key to this dictionary is an attribute name
            # each value is the value of this attribute name
            for key, value in kwargs.items():
                if key == "updated_at":
                    # convert string date to datetime object
                    # strptime (string parse time): Parse a string into a -
                    # datetime object given a corresponding format
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    value = datetime.strptime(value, "Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    # this happens because __class__ is no mandatory in output
                    continue
                setattr(self, key, value)
        else:
            # generate UUID
            self.id = str(uuid.uuid4())
            # Assign new instances with current datetime
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # new instance add a call to the new(self) method
            models.storage.new(self)

    def __str__(self):
        """ overriding the __str__ method that returns a custom string object """
        class_name = type(self).__name__
        mssg = "[{0}] ({1}) {2}".format(class_name, self.id, self.__dict__)
        return mssg

    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        # Define a dictionary and key __class__ that add to this dictionary with
        # the class name of the object
        tdic = {}
        tdic["__class__"] = type(self).__name__
        for n, i in self.__dict__.items():
            if isinstance(i, datetime):
                tdic[n] = i.isoformat()
            else:
                tdic[n] = 1
        return tdic
