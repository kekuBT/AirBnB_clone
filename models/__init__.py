#!/usr/bin/python3
""" create a unique FileStorage instance for your application """

from typing_extensions import Self
from models.engine.file_storage import FileStorage

storage = FileStorage
storage.reload(Self)
