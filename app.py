from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from config import Config
from models import db, User
from routes.addTestUser import addTestUserBlueprint
from routes.index import indexBlueprint
from routes.login import loginBlueprint
from routes.signup import signUpBlueprint
from utils.logger import Log

app = Flask(import_name=Config.APP_NAME, root_path=Config.APP_ROOT, static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATES_FOLDER)
app.secret_key = Config.APP_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Match WERKZEUG_LOGGER status
match Config.WERKZEUG_LOGGER:
    # If Werkzeug default logger is enabled
    case True:
        # Log that Werkzeug default logger is enabled
        Log.app("Werkzeug default logger is enabled")
    # If Werkzeug default logger is disabled
    case False:
        # Import getLogger from logging module
        from logging import getLogger

        # Log that Werkzeug default logger is disabled
        Log.app("Werkzeug default logger is disabled")
        # Disable the Werkzeug default logger
        getLogger("werkzeug").disabled = True
csrf = CSRFProtect(app)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


with app.app_context():
    db.create_all()

app.register_blueprint(indexBlueprint)
app.register_blueprint(addTestUserBlueprint)
app.register_blueprint(signUpBlueprint)
app.register_blueprint(loginBlueprint)

if __name__ == '__main__':
    Log.app(f"Running on http://{Config.APP_HOST}:{Config.APP_PORT}")
    Log.app("App started")
    app.run(debug=Config.DEBUG, host=Config.APP_HOST, port=Config.APP_PORT)
