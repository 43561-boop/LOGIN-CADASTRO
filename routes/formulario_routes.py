from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.formulario_controller import FormularioController

formulario_bp = Blueprint('formulario',__name__)

@formulario_bp.route('/', methods=['POST'])
@jwt_required()
def create_formulario():
    user_id = get_jwt_identity()
    return jsonify(FormularioController.create_formulario(user_id, request.get_json()))

@formulario_bp.route('/', methods=['GET'])
@jwt_required()
def get_formulario():
    user_id = get_jwt_identity()
    return jsonify(FormularioController.get_formulario(user_id))