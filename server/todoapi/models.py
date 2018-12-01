"""
models.py
- Data classes for the surveyapi application
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from todoapi.application import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    description=self.description,
                    completed=self.completed,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))
