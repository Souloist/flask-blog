from __future__ import absolute_import

from sqlalchemy import Column, Integer, String
from blog.models.meta import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    message = Column(String(120))

    def __init__(self, username, message):
        self.username = username
        self.message = message

    def __repr__(self):
        return "<User {}>".format(self.username)
