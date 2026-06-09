import os

# Flask Configuration
FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
DEBUG = FLASK_ENV == 'development'

# Database Configuration
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/elementary_treasury'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# Session Configuration
SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
PERMANENT_SESSION_LIFETIME = 3600  # 1 hour

# Application Settings
APP_NAME = 'Elementary Treasury System'
APP_VERSION = '1.0.0'
