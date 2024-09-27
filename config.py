import os
import secrets


class Config:
    APP_NAME = "FlaskBase"
    APP_VERSION = "0.0.1"
    APP_AUTHOR = "Doğukan Ürker"
    APP_HOST = "0.0.0.0"
    APP_PORT = 8080
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(APP_ROOT, "database.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UI_NAME = "bootstrap"
    STATIC_FOLDER = os.path.join(APP_ROOT, f"static")
    TEMPLATES_FOLDER = os.path.join(APP_ROOT, f"templates/{UI_NAME}")
    APP_SECRET_KEY = secrets.token_urlsafe(32)
    DEBUG = True
    LANGUAGES = ["tr", "en"]
    LOG_FOLDER_ROOT = "./logs"
    LOG_FILE_ROOT = os.path.join(LOG_FOLDER_ROOT, "log.log")
    LOG_APP_FILE_ROOT = os.path.join(LOG_FOLDER_ROOT, "app.log")
    LOG_SQL_FILE_ROOT = os.path.join(LOG_FOLDER_ROOT, "sql.log")
    LOG_INFO_FILE_ROOT = os.path.join(LOG_FOLDER_ROOT, "info.log")
    LOG_DANGER_FILE_ROOT = os.path.join(LOG_FOLDER_ROOT, "danger.log")
    LOG_SUCCESS_FILE_ROOT = os.path.join(LOG_FOLDER_ROOT, "success.log")
    LOG_WARNING_FILE_ROOT = os.path.join(LOG_FOLDER_ROOT, "warning.log")
    BREAKER_TEXT = ""
    CUSTOM_LOGGER = True  # Set to False to disable logging
    WERKZEUG_LOGGER = False
