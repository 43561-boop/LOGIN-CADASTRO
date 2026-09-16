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
    def get_user():
    user = user.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de usuarios.',
            'dados': [j.json() for j in user]
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

    def get_user_by_id(user_id):
        user = User.query.get(user_id)
    if user:
        response = make_response(
            json.dumps({
                'mensagem': 'Lista de usuario.',
                'dados': user.json()
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({'mensagem': 'Usuario não encontrado.', 'dados': {}}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    @staticmethod
    def create_user(user_cadastrado):
        novo_user= User(
        nickname=user_cadastrado['nickname'],
        password=user_cadastrado['password'],
        idade=user_cadastrado['idade']
    )
    db.session.add(novo_usuario)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Usuario cadastrado com sucesso.',
            'user': novo_user.json()
        }, ensure_ascii=False, sort_keys=False),
        201
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def update_user(user_id,user_cadastro):
    user = User.query.get(user_id)

    if not user:
        response = make_response(
            json.dumps({'mensagem': 'Usuario não encontrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    if not all(key in user_cadastrado for key in [ 'nickname','password', 'idade']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos, nickname, password e idade são obrigatórios.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'

        return response
    
    user.nickname = user_cadastrado['nickname']
    user.password = user_cadastrado['pasword']
    user.idade = user_cadastrado['idade']

    db.session.commit()

    response = make_response(
               json.dumps({
                'mensagem': 'Cadastro do usuario atualizado com sucesso.',
            'user': user.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

    @staticmethod

    def delete_user(user_id):
        user = User.query.get(user_id)
    if not user:
        response = make_response(
            json.dumps({'mensagem': 'Usuario não cadastrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(user)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Cadastro do usuario deletado com sucesso.',
            'dados': {'id': user_id}
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response