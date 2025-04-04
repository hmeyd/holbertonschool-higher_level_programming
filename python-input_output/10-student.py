#!/usr/bin/python3
"""
a class Student that defines a student by
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            my_list = {}
            for key in self.__dict__:
                if key in attrs:
                    my_list[key] = self.__dict__[key]
        return my_list
