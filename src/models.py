from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120))
    lastname: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    posts: Mapped[List["Post"]] = relationship(back_populates="author")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")
    followers: Mapped[List["Follower"]] = relationship(
        back_populates="user_to", foreign_keys="Follower.user_to_id"
    )
    following: Mapped[List["Follower"]] = relationship(
        back_populates="user_from", foreign_keys="Follower.user_from_id"
    )

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)  # aca creo la primary
    # aca la clave foranea del id de un user
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    # relacion con el user q hizo el post
    author: Mapped["User"] = relationship(back_populates="posts")
    media_items: Mapped[List["Media"]] = relationship(back_populates="post")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")


class Media(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        type: Mapped[str] = mapped_column(String(20), nullable=False)
        url: Mapped[str] = mapped_column(String(255), nullable=False)
        post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
        post: Mapped["Post"] = relationship(back_populates="media_items")


class Comment(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        comment_text: Mapped[str] = mapped_column(String(200), nullable=False)
        author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
        post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))

        author: Mapped["User"] = relationship(back_populates="comments")
        post: Mapped["Post"] = relationship(back_populates="comments")


class Follower(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        user_from_id: Mapped[int] = mapped_column(
            ForeignKey("user.id"), nullable=False)
        user_to_id: Mapped[int] = mapped_column(
            ForeignKey("user.id"), nullable=False)
        user_from: Mapped["User"] = relationship(
        back_populates="following", foreign_keys=[user_from_id]
    )
        user_to: Mapped["User"] = relationship(
        back_populates="followers", foreign_keys=[user_to_id]
    )
        
from eralchemy2 import render_er
render_er(db.Model, "diagram.png")