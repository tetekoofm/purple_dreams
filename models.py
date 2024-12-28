from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Initialize the SQLAlchemy object
db = SQLAlchemy()

class Upcoming(db.Model):
    __tablename__ = 'upcoming'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(300), nullable=True)
    description = db.Column(db.Text, nullable=True)

class Memory(db.Model):
    __tablename__ = 'memory'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Memory {self.title}>'
    
class Milestone(db.Model):
    __tablename__ = 'milestone'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Milestone {self.title}>'
    
class Discography(db.Model):
    __tablename__ = 'discography'

    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable=False)
    album_name = db.Column(db.String(200), nullable=False)
    song_name = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.String(10), nullable=False)  # Store duration as a string

    def __repr__(self):
        return f'<Discography {self.song_name}>'

class MusicVideo(db.Model):
    __tablename__ = 'musicvideo'

    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable=False)
    video_name = db.Column(db.String(255), nullable=False)
    youtube_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<MusicVideo {self.name}>'

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
    
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(50), nullable=False, default='Created')
    created_at = db.Column(db.DateTime, server_default=db.func.now())