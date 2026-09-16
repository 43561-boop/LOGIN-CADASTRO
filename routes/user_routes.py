from flask import Blueprint, request, jsonify
from controllers.user_controller import UserControllers
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('users',__name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify(UserControllers.register_user(request.get_json()))

@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify(UserControllers.login_user(request.get_json()))

@user_bp.route('/me', methods=['GET'])
@jwt_required()  
def get_user():
    user_id = get_jwt_identity()
    return jsonify(UserController.get_user(user_id))