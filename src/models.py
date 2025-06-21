from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120))
    lastname: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    favorite_list: Mapped[List["Favorites"]] = relationship("Favorite", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(100))
    terrain: Mapped[str] = mapped_column(String(100))

    favorites: Mapped[List["Favorites"]] = relationship("Favorite", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain
        }

class People(db.Model):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(20))
    gender: Mapped[str] = mapped_column(String(20))

    favorites: Mapped[List["Favorites"]] = relationship("Favorite", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
class Vehicle(db.Model):
    __tablename__ = "vehicle"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100))
    vehicle_class: Mapped[str] = mapped_column(String(100))
    manufacturer: Mapped[str] = mapped_column(String(100))

    favorites: Mapped[List["Favorites"]] = relationship("Favorite", back_populates="vehicle")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer
        }         


class Favorites(db.Model):
    __tablename__ = "favorite"
    id: Mapped[int] = mapped_column(primary_key=True)      
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    character_id: Mapped[Optional[int]] = mapped_column(ForeignKey("people.id"))

    user: Mapped["User"] = relationship("User", back_populates="favorite_list")
    planet: Mapped[Optional["Planet"]] = relationship("Planet", back_populates="favorites")
    character: Mapped[Optional["People"]] = relationship("People", back_populates="favorites")
    vehicle_id: Mapped[Optional[int]] = mapped_column(ForeignKey("vehicle.id"))
    vehicle: Mapped[Optional["Vehicle"]] = relationship("Vehicle", back_populates="favorites")

    def serialize(self):
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "planet": self.planet.serialize() if self.planet else None,
            "character": self.character.serialize() if self.character else None,
            "vehicle": self.vehicle.serialize() if self.vehicle else None
        }