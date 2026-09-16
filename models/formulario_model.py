import sqlite3
from database.db import get_db_connection

class FormularioModel:

    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO formulario (user_id, nome, email, data_nascimento cpf, genero)
                            VALUES (?,?,?,?,?,?)''',
                        (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close

    @staticmethod
    def find_by_user_id(user_id):
        conn = get_db_connection()
        formulario = conn.execute('SELECT * FROM formularios WHERE user_id = ?', (user_id,)).fetchone()

    @staticmethod
    def find_by_id(formulario_id):
        conn = get_db_connection()
        formlario = conn.execute('SELECT * FROM formularios WHERE id = ? ', (formulario_id,)). fetchone()