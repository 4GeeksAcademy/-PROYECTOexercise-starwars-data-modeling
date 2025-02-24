import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table, BigInteger  
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    lastname = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    password = Column(String, nullable=False)
    Subscription_Date = Column(Date, nullable=False)
    favs = relationship("Favorito", backref= "user")


class Person(Base):
    __tablename__ = "person"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[Integer] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column(nullable=False)
    address: Mapped["Address"] = relationship(back_populates="person")


class Address(Base):
    __tablename__ = "address"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[Integer] = mapped_column(primary_key=True)
    street_name: Mapped[String]
    street_number: Mapped[String]
    post_code: Mapped[String] = mapped_column(nullable=False)
    person_id: Mapped[Integer] = mapped_column(ForeignKey("person.id"))
    person: Mapped["Person"] = relationship(back_populates="address")


    class Planeta(Base):
    __tablename__ ="planetas"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    climate = Column(String, nullable=False)
    population = Column(String, nullable=False)
    terreno = Column(String, nullable=False)
    Todos = relationship("Favorito", backref= "planetas")

    class todos(Base):
    __tablename__= "Todos"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    td_person = Column(Integer, ForeignKey("person.id"), primary_key=True)
    td_planeta = Column(Integer, ForeignKey("planeta.id"), primary_key=True)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
