from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(os.getenv('APP_NAME'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

class Users(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

@app.route('/')
def index():
    fruits = ['Apel', 'Jeruk', 'Pisang', 'Duren']    
    
    return render_template('index.html', fruits=fruits, app_name=os.getenv('APP_NAME'), db=Users.query.all()) 

# @app.route('/halaman_kedua')
# def halaman_kedua():
#     return render_template('halaman_kedua.html')

if __name__ == '__main__':
    app.run()