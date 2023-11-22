#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ The user class, contains user information """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Define the relationship with the Place class
    places = relationship("Place", back_populates="user", cascade="all, delete-orphan")

# Import Place after defining the User class to avoid circular import
from models.place import Place

# Add a foreign key constraint to the Place class
Place.user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
Place.user = relationship("User", back_populates="places")
