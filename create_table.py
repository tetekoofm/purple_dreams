# create_table.py
from app import db, app
from models import Product, Discography
import os

# Set the database URI to use taekook.db
project_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(project_dir, 'instance', 'taekook.db')

# Create all tables in taekook.db
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_file}"
db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()
    print("Tables created successfully in taekook.db!")
