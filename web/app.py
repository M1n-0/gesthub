import os
import uuid
import json
from flask import Flask, redirect, url_for, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
ANNOUNCE_FILE = os.path.join(os.path.dirname(__file__), "annonces.json")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:flaskpass@mariadb/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

db = SQLAlchemy(app)

# Configuration de Authlib
oauth = OAuth(app)

keycloak = oauth.register(
    name='keycloak',
    client_id='flask-app',
    client_secret='T5G5jzCBiphnBNh9uuj0f6YNc9HrP8r4',
    server_metadata_url='https://keycloak.ninolbt.com/realms/gesthub/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email',
    }
)

@app.route('/')
def index():
    user = session.get('user')
    if user:
        return render_template('view/index.html', user=user)
        
    return redirect(url_for('login'))

@app.route('/login')
def login():
    nonce = uuid.uuid4().hex
    session['nonce'] = nonce
    redirect_uri = url_for('auth', _external=True, _scheme='https')
    return keycloak.authorize_redirect(redirect_uri, nonce=nonce)

@app.route('/auth')
def auth():
    token = keycloak.authorize_access_token()
    nonce = session.pop('nonce', None)
    userinfo = keycloak.parse_id_token(token, nonce=nonce)
    session['user'] = userinfo
    session["id_token"] = token.get("id_token")
    app.logger.debug(f"User info: {userinfo}")
    return redirect('/')

@app.route("/logout")
def logout():
    id_token = session.get("id_token")
    print("ID Token Hint:", id_token)
    session.clear()
    return redirect(
        f"https://keycloak.ninolbt.com/realms/gesthub/protocol/openid-connect/logout"
        f"?post_logout_redirect_uri=https://dashboard.ninolbt.com"
        f"&id_token_hint={id_token}"
    )
def load_announces():
    try:
        with open(ANNOUNCE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_announces(announces):
    with open(ANNOUNCE_FILE, "w", encoding="utf-8") as f:
        json.dump(announces, f, ensure_ascii=False, indent=2)

def get_next_id(announces):
    return max((a.get("id", 0) for a in announces), default=0) + 1

@app.route("/api/annonces", methods=["GET"])
def get_announces():
    return jsonify(load_announces())

@app.route("/api/annonces", methods=["POST"])
def create_annonce():
    user = session.get("user")
    if not user or "/admin" not in user.get("groups", []):
        return jsonify({"error": "unauthorized"}), 403
    data = request.json
    if not data.get("text"):
        return jsonify({"error": "missing text"}), 400

    announces = load_announces()
    new_announce = {
        "id": get_next_id(announces),
        "text": data["text"],
        "author": user.get("preferred_username", "admin")
    }
    announces.append(new_announce)
    save_announces(announces)
    return jsonify({"status": "ok", "announce": new_announce})

@app.route("/api/annonces/<int:annonce_id>", methods=["DELETE"])
def delete_annonce(annonce_id):
    user = session.get("user")
    if not user or "/admin" not in user.get("groups", []):
        return jsonify({"error": "unauthorized"}), 403
    announces = load_announces()
    announces = [a for a in announces if a["id"] != annonce_id]
    save_announces(announces)
    return jsonify({"status": "deleted"})

@app.route("/api/annonces/<int:annonce_id>", methods=["PUT"])
def edit_annonce(annonce_id):
    user = session.get("user")
    if not user or "/admin" not in user.get("groups", []):
        return jsonify({"error": "unauthorized"}), 403
    data = request.json
    announces = load_announces()
    found = False
    for a in announces:
        if a["id"] == annonce_id:
            a["text"] = data.get("text", a["text"])
            found = True
    if not found:
        return jsonify({"error": "not found"}), 404
    save_announces(announces)
    return jsonify({"status": "updated"})

@app.route("/api/is_admin")
def is_admin():
    user = session.get("user")
    return jsonify({"admin": "/admin" in user.get("groups", [])})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
