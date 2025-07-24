import pprint
from operator import attrgetter

from models.cliente import PessoaFisica, PessoaJuridica


def inserir_registro(conexao, cursor, cliente):
    try:
        if isinstance(cliente, PessoaFisica):
            get_attrs = attrgetter("nome", "cpf", "data_nascimento", "endereco")
            data = get_attrs(cliente)
            cursor.execute(
                "INSERT INTO pessoas_fisicas (nome, cpf, data_nascimento, endereco) \
                    VALUES (?, ?, ?, ?);",
                data,
            )
        elif isinstance(cliente, PessoaJuridica):
            get_attrs = attrgetter("nome_social", "cnpj", "razao_social", "endereco")
            data = get_attrs(cliente)
            cursor.execute(
                "INSERT INTO pessoas_fisicas (nome_social, cnpj, razao_social, \
                    endereco) VALUES (?, ?, ?, ?);",
                data,
            )
        conexao.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        conexao.rollback()


def listar_registros(cursor, cliente):
    if isinstance(cliente, PessoaFisica):
        clientes = cursor.execute("SELECT * FROM pessoas_fisicas;")
    elif isinstance(cliente, PessoaJuridica):
        clientes = cursor.execute("SELECT * FROM pessoas_juridicas;")
    return clientes


def encontrar_registro_por_id(cursor, cliente, id):
    if isinstance(cliente, PessoaFisica):
        cursor.execute("SELECT * FROM pessoas_fisicas WHERE id = ?;", (id,))
    elif isinstance(cliente, PessoaJuridica):
        cursor.execute("SELECT * FROM pessoas_juridicas WHERE id = ?;", (id,))
    return cursor.fetchone()
