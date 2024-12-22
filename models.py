from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Initialize the SQLAlchemy object
db = SQLAlchemy()

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Define the Discography model
class Discography(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable=False)
    album_name = db.Column(db.String(200), nullable=False)
    song_name = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.String(10), nullable=False)  # Store duration as a string

    def __repr__(self):
        return f'<Discography {self.song_name}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(50), nullable=False, default='Created')
    created_at = db.Column(db.DateTime, server_default=db.func.now())