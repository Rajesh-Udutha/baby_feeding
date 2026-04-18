#  running migrations
from config import Config
from models import db

from models.user import User
from models.babies import Babies
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt

from flask import Flask, jsonify, request, session, url_for

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

jwt = JWTManager(app)

black_list = set()

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
            access_token = create_access_token(identity = str(user.id))
            refresh_token = create_refresh_token(identity = str(user.id))

            return jsonify({"message" : "Login Successfull", 
                            'refresh_token':refresh_token, 'access_token':access_token
                            })
        else:
            return jsonify({"message":"Authentication Failed"})
        
@app.route('/api/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    return jsonify({"Message":"Profile ", "user_id":user_id, "email":user.email})

@app.route("/api/refresh", methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    new_access_token = create_access_token(identity = str(user_id))

    return jsonify({"access_token":new_access_token})


@app.route("/api/logout", methods=["GET"])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    black_list.add(jti)
    return jsonify({"message":"Logged out successfully."})

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return jwt_payload["jti"] in black_list



@app.route("/api/add_baby", methods=["POST"])
@jwt_required()
def add_baby():
    data = request.get_json()
    baby = Babies(user_id = data['user_id'], name=data["name"], dob=data["dob"])
    db.session.add(baby)
    db.session.commit()
    return jsonify({"message":"Baby Added successfully"})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)