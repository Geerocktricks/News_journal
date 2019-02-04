from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,instance_relative_config = True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

botstrap = Bootstrap(app)

from app import views
from app import error