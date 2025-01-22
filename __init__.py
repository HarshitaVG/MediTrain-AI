from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes
