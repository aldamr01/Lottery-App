from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    fruits = ['Apel', 'Jeruk', 'Pisang', 'Duren']
    return render_template('index.html', fruits=fruits) 

# @app.route('/halaman_kedua')
# def halaman_kedua():
#     return render_template('halaman_kedua.html')

if __name__ == '__main__':
    app.run()