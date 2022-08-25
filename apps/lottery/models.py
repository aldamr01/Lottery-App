# from flask_sqlalchemy import SQLAlchemy
from basemodel import db
from datetime import datetime

class Lottery(db.Model):
    
    __tablename__ = 'lottery'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    max_participant = db.Column(db.Integer, nullable=False)        
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    
    participants = db.relationship('LotteryParticipants', backref='lottery', lazy=True)

class LotteryParticipants(db.Model):
    
    __tablename__ = 'lottery_participants'
    
    id = db.Column(db.Integer, primary_key=True)
    lottery_id = db.Column(db.Integer, db.ForeignKey('lottery.id'), nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())