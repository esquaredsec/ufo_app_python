from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Define a model for UFO sightings
class UFOReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))
    posted = db.Column(db.String(255))
    summary = db.Column(db.Text)

    def __init__(self, date_time, city, state, country, posted, summary):
        self.date_time = date_time
        self.city = city
        self.state = state
        self.country = country
        self.posted = posted
        self.summary = summary
