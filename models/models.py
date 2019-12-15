from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Create table(average age, min age, max age)
class AgeMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_age = db.Column(db.Float, unique=False)
    min_age = db.Column(db.Integer, unique=False)
    max_age = db.Column(db.Integer, unique=False)


class HeightMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_height = db.Column(db.Float, unique=False)
    min_height = db.Column(db.Integer, unique=False)
    max_height = db.Column(db.Integer, unique=False)


class Correlation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age_rating_correlation = db.Column(db.Float, unique=False)
    age_pace_correlation = db.Column(db.Float, unique=False)
    pass_short_long_correlation = db.Column(db.Float, unique=False)


class Variance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variance = db.Column(db.String, unique=False)
    standard_dev = db.Column(db.String, unique=False)
