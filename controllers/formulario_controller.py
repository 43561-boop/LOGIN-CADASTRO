from models.formulario_model import FormularioModel

class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')
        email = data.get('email')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        genero = data.get('genero')

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatorio"}, 400
        
        formulario = FormularioModel.creat_formulario(user_id, nome, email, data_nascimento, cpf, genero)
        if formulario:
            return{"mensagem": "Formulario criado com sucesso"}, 201
        return{"error": "Erro ao criar formulario"}, 500

    @staticmethod
    def get_formulario(user_id):

        formulario = FormularioModel.find_by_user_id(user_id)
        if formulario:
            return {"id": formulario['id'], "nome": formulario['nome'], "email": formulario['email'],
            "data_nascimento": formulario['data_nascimento'], "cpf": formulario['cpf'],
            "genero": formulario['genero']}, 200
            return {"error": "Formulario não encontrado"}, 400

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