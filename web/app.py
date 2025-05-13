import os
from flask import Flask, redirect, url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:flaskpass@mariadb/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

db = SQLAlchemy(app)

# Configuration de Authlib
oauth = OAuth(app)

keycloak = oauth.register(
    name='keycloak',
    client_id='flask-app',
    client_secret='6R70kt1x9KjYpccZCMnPvJAGiJFzRHjE',
    server_metadata_url='http://keycloak.localhost/realms/gesthub/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email',
    }
)

@app.route('/')
def index():
    user = session.get('user')
    if user:
        return render_template('/view/index.html', user=user)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    nonce = uuid.uuid4().hex
    session['nonce'] = nonce
    redirect_uri = url_for('auth', _external=True)
    return keycloak.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = keycloak.authorize_access_token()
    nonce = session.pop('nonce', None)
    userinfo = keycloak.parse_id_token(token)
    session['user'] = userinfo
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
