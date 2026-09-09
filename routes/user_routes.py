from flask import Blueprint, request, jsonify
from controllers.user_controller import UserControllers

user_bp = Blueprint('users',__name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify(UserControllers.register_user(request.get_json()))

@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify(UserControllers.login_user(request.get_json()))