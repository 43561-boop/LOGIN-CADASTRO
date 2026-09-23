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
        def delete_formulario(user_id, data):
            nome = data.get('nome')
            email = data.get('email')
            data_nascimento = data.get('data_nascimento')
            cpf = data.get('cpf')
            genero = data.get('genero')

            if not nome or not email or not data_nascimento or not cpf or not genero:
                return {"error": "Todos os campos foram deletado"}, 400
        
            formulario = FormularioModel.delete_formulario(user_id, nome, email, data_nascimento, cpf, genero)
            if formulario:
                return{"mensagem": "Formulario deletado com sucesso"}, 201
            return{"error": "Erro ao deletar formulario"}, 500

    @staticmethod
    def delete_formulario(user_id):

        formulario = FormularioModel.delete_id(user_id)
        if formulario:
            return {"id": formulario['id'], "nome": formulario['nome'], "email": formulario['email'],
            "data_nascimento": formulario['data_nascimento'], "cpf": formulario['cpf'],
            "genero": formulario['genero']}, 200
            return {"error": "Formulario não deletado"}, 400
 
        @staticmethod
        def update_formulario(user_id, data):
            nome = data.get('nome')
            email = data.get('email')
            data_nascimento = data.get('data_nascimento')
            cpf = data.get('cpf')
            genero = data.get('genero')

            if not nome or not email or not data_nascimento or not cpf or not genero:
                return {"error": "Todos os campos foram atualizados"}, 400
        
            formulario = FormularioModel.atualizado_formulario(user_id, nome, email, data_nascimento, cpf, genero)
            if formulario:
                return{"mensagem": "Formulario atualilzado com sucesso"}, 201
            return{"error": "Erro ao atualizar formulario"}, 500

    @staticmethod
    def update_formulario(user_id):

        formulario = FormularioModel.update_id(user_id)
        if formulario:
            return {"id": formulario['id'], "nome": formulario['nome'], "email": formulario['email'],
            "data_nascimento": formulario['data_nascimento'], "cpf": formulario['cpf'],
            "genero": formulario['genero']}, 200
            return {"error": "Formulario não atualizado"}, 400