from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Workout(db.Model):
    """
    Represents a single workout/exercise log in the database.
    Stores the name, sets, reps, weight, and automatically tracks total volume.
    """
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    
    # Automatically setting the date to the current UTC time if not manually provided
    date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    total_volume = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def calculate_volume(self):
        """Helper method to calculate the total kg/lbs lifted for this exercise entry."""
        return self.sets * self.reps * self.weight
