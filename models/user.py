#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(string(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(string(128), nullable=True)
    last_name = Column(string(128), nullable=True)

    places = relationship('Place' backref='user', cascade='all, delete-orphan')
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="user",
                               cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """Getter attribute reviews.Returns the list of Review instances"""
            from models import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.user_id == self.id:
                    review_list.append(review)
            return review_list
