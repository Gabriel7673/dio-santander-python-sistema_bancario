import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def conectar_db(file_name):
    conexao = sqlite3.connect(ROOT_PATH / file_name)
    cursor = conexao.cursor()
    cursor.row_factory = sqlite3.Row
    return conexao, cursor


def criar_tabela(conexao, cursor, nome_tabela, colunas):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas})")
    conexao.commit()


conexao, cursor = conectar_db("clientes.db")
criar_tabela(
    conexao,
    cursor,
    nome_tabela="pessoas_fisicas",
    colunas="id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL, \
        cpf VARCHAR(11) UNIQUE, data_nascimento Date, endereco VARCHAR(150) \
        NOT NULL",
)

criar_tabela(
    conexao,
    cursor,
    nome_tabela="pessoas_juridicas",
    colunas="id INTEGER PRIMARY KEY AUTOINCREMENT, nome_social VARCHAR(100) NOT NULL, \
        cnpj VARCHAR(20) UNIQUE, razao_social VARCHAR(100), \
        endereco VARCHAR(150)",
)
