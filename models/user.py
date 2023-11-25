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

    places = relationship("Place", back_populates="user", cascade="all, delete-orphan")

# Add or replace the class attributes
User.__tablename__ = "users"
User.email = Column(String(128), nullable=False)
User.password = Column(String(128), nullable=False)
User.first_name = Column(String(128), nullable=True)
User.last_name = Column(String(128), nullable=True)
