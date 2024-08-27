import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table,Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

 #Relacion de muchos a muchos entre el  User con Folower un usuario puede seguir a varios usuarios y asi mismo estos usuarios pueden seguirle a él un a otros 
followers = Table('followers',
    Base.metadata,            
    Column('user_from_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('user_to_id', Integer, ForeignKey('user.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id =Column(Integer, primary_key=True)
    username =Column(String(50), nullable=False)
    firstname =Column(String(50), nullable=False)
    lastname =Column(String(50), nullable=False)
    email =Column(String(255), nullable=False)

#La class Follower ya no seria necesario declararla
# class Follower(Base):
#     __tablename__ = 'follower'
#     id = Column(Integer, primary_key=True)

#Relacion de uno a muchos entre user y post un usuario puede hacer muchos post 

class Post(Base):
    __tablename__ = 'post'
    id =Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

#Relacion de uno a muchos entre user y comment un usuario puede hacer muchos comment
#Relacion de uno a muchos entre post y commet un post puede tener muchos comments
class Comment(Base):
    __tablename__ = 'comment'
    id =Column(Integer, primary_key=True)
    Comment_text =Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

#Relacion de uno a muchos entre post y media un post puede tener muchos fotos 
class Media(Base):
    __tablename__ = 'media'
    id =Column(Integer, primary_key=True)
    type = Column(Enum('image', 'video', 'audio', name='media_types'), nullable=False)  # Definición de type como enum
    url =Column(String(255), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
