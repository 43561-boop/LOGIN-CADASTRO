from werkzeug.security import generate_password_hash, check_password_hash
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
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha inválidos"}, 401
    
    @staticmethod
    def get_user(user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            return {"id": user['id'], "username": user['username']}, 200
        return {"error": "Usuário não encontrado"}, 404

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
            return {"error": "Nome de usuário e senha foram deletado"}, 400
        
        user = UserModel.find_by_username(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha não deletado"}, 401
    

    @staticmethod
    def delete_login_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são deletados"}, 400
        
        user = UserModel.find_by_username(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha deletados"}, 401
    
    @staticmethod
    def delete_user(user_id):
        user = UserModel.delete_id(user_id)
        if user:
            return {"id": user['id'], "username": user['username']}, 200
        return {"error": "Usuário não deletaods"}, 404

        def delete_register_user(data):
             username = data.get('username')
             password = data.get('password')

        if not username or password:
            return {"error": "Nome de usuário e senha não foram deletados"}, 400
        hashed_password = generate_password_hash(password)

        if UserModel.create_user(username, hashed_password):
            return {"mensagem": "Usuário deletado com sucesso"}, 201
        
        return {"error": "Nome de usuário já deletado"}, 400
    
    @staticmethod
    def delete_login_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha foram deletado"}, 400
        
        user = UserModel.delete_username(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha não deletado"}, 401
    
    @staticmethod
    def update_login_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são atualizados"}, 400
        
        user = UserModel.update_username(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha atualizados"}, 401
    
    @staticmethod
    def update_user(user_id):
        user = UserModel.update.id(user_id)
        if user:
            return {"id": user['id'], "username": user['username']}, 200
        return {"error": "Usuário não deletaods"}, 404

        def update_register_user(data):
             username = data.get('username')
             password = data.get('password')

        if not username or password:
            return {"error": "Nome de usuário e senha não foram atualizado"}, 400
        hashed_password = generate_password_hash(password)

        if UserModel.create_user(username, hashed_password):
            return {"mensagem": "Usuário atualizado com sucesso"}, 201
        
        return {"error": "Nome de usuário já atualizado"}, 400
    
    @staticmethod
    def update_login_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha foram deletado"}, 400
        
        user = UserModel.update_username(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha não atualizado"}, 401
