from flask import Flask
app = Flask(__name__)
from Form import views, database_helper
app.debug = True
