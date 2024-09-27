from flask import Blueprint
from flask_login import login_required

from models import User
from utils.generateID import generateID
from utils.passwordHash import hashPassword

addTestUserBlueprint = Blueprint('addTestUser', __name__)


@addTestUserBlueprint.route('/addTestUser', methods=['GET', 'POST'])
@login_required
def addTestUser():
    new_user = User(id=generateID("dogukanurker"),  # Unique identifier
                    username="dogukanurker",  # Unique username
                    email="dogukanurker@example.com",  # Unique email address
                    password=hashPassword("password"),  # Hashed password
                    role="user",  # Default role
                    firstName="Dogukan",  # Optional first name
                    lastName="Urker",  # Optional last name
                    profileImage='/static/img/defaultProfile.png',  # Default profile image
                    bio="This is a sample bio.",  # Optional bio
                    isActive=True,  # Account is active
                    isVerified=False,  # Email is not verified
                    isDeleted=False,  # Account is not marked as deleted
                    themePreference="dark",  # Default theme preference
                    languagePreference="tr"  # Default language preference
                    )
    # db.session.add(new_user)
    # db.session.commit()
    return "user added"
