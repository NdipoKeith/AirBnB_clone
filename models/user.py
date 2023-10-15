#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class for managing user objects
    Attributes:
        email (str): the email of the user
        password (str): the password of the user
        first_name (str): the first name of the user
        last_name (str): the last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
