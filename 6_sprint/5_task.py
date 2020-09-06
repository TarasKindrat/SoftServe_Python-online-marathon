"""
Create context manager class SerializeManager with attributes filename and type for serializing
 python object to different formats.
For defining format create enum FileType with values JSON, BYTE. Create function
serialize(object, filename, fileType).
This function should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will
 contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json"
and text "String"
"""

import json
import pickle
from enum import Enum


class FileType(Enum):
    JSON = "JSON"
    BYTE = "BYTE"


class SerializeManager:
    def __init__(self, file_name, type_for_serializing):
        self.file_name = file_name
        self.type_for_serializing = type_for_serializing

    def __enter__(self):
        if self.type_for_serializing == FileType.BYTE:
            self.file = open(self.file_name, 'wb')
        if self.type_for_serializing == FileType.JSON:
            self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


def serialize(object, filename, fileType):
    if  fileType == FileType.BYTE:
        with SerializeManager(filename, fileType) as f:
            pickle.dump(object, f)
    if  fileType == FileType.JSON:
        with SerializeManager(filename, fileType) as f:
            json.dump(object, f)


#serialize("hekko", "pikl", FileType.BYTE)

serialize("String", "1", FileType.JSON)

user_dict = {"name": "Hallo", "id": 2}
serialize(user_dict, "2222", FileType.JSON)