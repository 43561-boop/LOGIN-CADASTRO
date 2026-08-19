from wekzeug.security import generate_password_hash, cheack_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import UserModel

class UserControllers:

    @staticmethod
    def register_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or password:
            return {"error": "Nome de usuário e senha não obrigatório"}, 400
        hashed_password = generate_password_hash(password)

        if UserModel.create_user(username, hashed_password):
            return {"mensagem": "Usuário registrado com sucesso"}, 201
        
        return {"error": "Nome de usuário já existente"}, 400
    
    @staticmethod
    def login_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"}, 400
        
        user = UserModel.find_by_username(username)
        if user and cheack_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha inválidos"}, 401