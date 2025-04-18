# flask-app/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:flaskpass@mariadb/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

    @app.route('/')
    def index():
        return render_template('index.html')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')
