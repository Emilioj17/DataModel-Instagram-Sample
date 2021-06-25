import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo = Column(String(50), nullable=False)
    facebook = Column(String(50), nullable=False)
    whatsapp = Column(String(50), nullable=False)
    app_id = Column(Integer, ForeignKey('apps.id'))

class App(Base):
    __tablename__ = 'apps'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    posts_from_others_id = Column(Integer, ForeignKey('posts_from_others.id'))
    users_followed_id = Column(Integer, ForeignKey('users_followed.id'))
    album_id = Column(Integer, ForeignKey('albumes.id'))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    tags_id = Column(Integer, ForeignKey('tags.id'))
    likes_id = Column(Integer, ForeignKey('likes.id'))
    comentarios_id = Column(Integer, ForeignKey('comentarios.id'))
    album_id = Column(Integer, ForeignKey('albumes.id'))

    def to_dict(self):
        return {}

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    tags = Column(String(250))

    def to_dict(self):
        return {}

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    likes = Column(Integer)

    def to_dict(self):
        return {}

class Album(Base):
    __tablename__ = 'albumes'
    id = Column(Integer, primary_key=True)
    album = Column(String(250))

    def to_dict(self):
        return {}

class Comentario(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    comentarios = Column(String(250))

    def to_dict(self):
        return {}
        
class Post_From_Others(Base):
    __tablename__ = 'posts_from_others'
    id = Column(Integer, primary_key=True)
    users_followed_id = Column(Integer, ForeignKey('users_followed.id'))
    tags = Column(String(50))
    likes = Column(Integer)
    comentarios = Column(String(250))

    def to_dict(self):
        return {}

class User_Followed(Base):
    __tablename__ = 'users_followed'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e