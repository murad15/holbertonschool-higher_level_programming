#!/usr/bin/env python3
import json
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
      
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.UnpicklingError, EOFError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, PermissionError, pickle.UnpicklingError, EOFError):
            return None

    
