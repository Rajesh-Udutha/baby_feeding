#  running migrations
from config import Config
from models import db

from models.user import User

from flask_migrate import Migrate

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def home():
    return "Hello, Baby Feeding App"

@app.route("/api/hello", methods=['GET'])
def hello():
    return jsonify({"message":"Hello API from Flask"}) 


@app.route("/api/register", methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        user = User(email=data["email"])
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"User created successfully"})
    
@app.route("/api/login", methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(email = data['email']).first()

        if user and user.check_password(data['password']):
            return jsonify({"message" : "Login Successfull"})
        else:
            return jsonify({"message":"Authentication Failed"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)