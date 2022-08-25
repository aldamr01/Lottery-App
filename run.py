from datetime import datetime
from config import AppConfig, GeneralConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template

app = Flask(GeneralConfig.APP_NAME)
app.config.from_object(AppConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
        

@app.route('/')
def index():
    fruits = ['Apel', 'Jeruk', 'Pisang', 'Duren']    
    
    return render_template('index.html', fruits=fruits, app_name=GeneralConfig.APP_NAME, ) 

# @app.route('/halaman_kedua')
# def halaman_kedua():
#     return render_template('halaman_kedua.html')

if __name__ == '__main__':    
    db.create_all()
    app.run()