from time import time

from flask_login import UserMixin
from sqlalchemy.types import JSON

from utils.passwordHash import checkPassword
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Unique identifier for each user (Primary Key)
    id = db.Column(db.String, unique=True, nullable=False, primary_key=True)

    # User's unique username
    username = db.Column(db.String, unique=True, nullable=False)

    # User's unique email address
    email = db.Column(db.String, unique=True, nullable=False)

    # Hashed password for authentication
    password = db.Column(db.String, nullable=False)

    # Role of the user (e.g., admin, user)
    role = db.Column(db.String, default="user", nullable=False)

    # User's first name (optional, default is 'Jamie')
    firstName = db.Column(db.String, default='Jamie')

    # User's last name (optional, default is 'Doe')
    lastName = db.Column(db.String, default='Doe')

    # Short bio or description provided by the user (optional)
    bio = db.Column(db.String, nullable=True)

    # Path to the user's profile image (default image provided)
    profileImage = db.Column(db.String, default='/static/img/defaultProfile.png')

    # Timestamp of when the account was created (float)
    createdAt = db.Column(db.Float, default=time())

    # Timestamp of when the account was last updated (float)
    updatedAt = db.Column(db.Float, default=time(), onupdate=time())

    # Timestamp of the user's last login (float)
    lastLogin = db.Column(db.Float, nullable=True)

    # List of timestamps(floats) representing user's login history
    logins = db.Column(JSON, default=list)

    # Indicates whether the user's account is active
    isActive = db.Column(db.Boolean, default=True)

    # Indicates whether the user's email has been verified
    isVerified = db.Column(db.Boolean, default=False)

    # Indicates whether the account is marked as deleted (soft delete)
    isDeleted = db.Column(db.Boolean, default=False)

    # User's preference for theme (light or dark mode)
    themePreference = db.Column(db.String, default="light")

    # User's preferred language (default is English)
    languagePreference = db.Column(db.String, default="en")

    def addLogin(self):
        currentTime = time()
        self.lastLogin = currentTime

        # Ensure that logins is initialized as a list if it is None
        if self.logins is None:
            self.logins = []

        # Append the new login time to the logins list
        self.logins.append(currentTime)

        # Commit the changes to the database
        db.session.commit()

    def matchPassword(self, password):
        return checkPassword(hashedPassword=self.password, password=password)

    def __repr__(self):
        return f"<User {self.username}>"
