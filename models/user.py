#!/usr/bin/python3
"""User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Is a User.

    Attributes:
        email (str): User email of .
        password (str): User password of the .
        first_name (str): User first name.
        last_name (str): User last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
