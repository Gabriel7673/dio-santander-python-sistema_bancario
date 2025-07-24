from data.iniciador_tabelas import conectar_db
from data.operacoes import inserir_registro
from models.cliente import PessoaFisica, PessoaJuridica
from models.conta import ContaCorrente
from utils.utils import validar_para_conta, validar_usuario

usuarios_fisicos = []
usuarios_juridicos = []
conexao, cursor = conectar_db("clientes.db")


def cadastrar_usuario():
    tipo = """
(1) Pessoa Física
(2) Pessoa Jurídica
=> """
    pessoa = input(tipo)
    match pessoa:
        case "1":
            return cadastrar_pessoa_fisica()
        case "2":
            return cadastrar_pessoa_juridica()
        case _:
            print("Opção inválida.")
            return


def cadastrar_pessoa_fisica():
    print("Seja bem vindo! Por favor digite seus dados:")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    valida, msg = validar_usuario(usuarios_fisicos, cpf)

    if valida:
        usuario = PessoaFisica(
            cpf,
            nome,
            data_nascimento,
            endereco,
        )
        inserir_registro(conexao, cursor, usuario)
        usuarios_fisicos.append(usuario)

    return msg


def cadastrar_pessoa_juridica():
    print("Seja bem vindo! Por favor digite seus dados:")
    cnpj = input("CNPJ: ")
    nome_social = input("Nome Social: ")
    razao_social = input("Razão Social: ")
    endereco = input("Endereço: ")

    valida, msg = validar_usuario(usuarios_juridicos, cnpj)

    if valida:
        usuario = PessoaJuridica(
            cnpj,
            nome_social,
            razao_social,
            endereco,
        )
        inserir_registro(conexao, cursor, usuario)
        usuarios_juridicos.append(usuario)

    return msg


def entrar_usuario():
    cpf = input("CPF: ")

    cpf_valido, _ = validar_para_conta(usuarios_fisicos, cpf)

    if cpf_valido:
        for usuario in usuarios_fisicos:
            if cpf == usuario.cpf:
                return usuario
    print("CPF não registrado.")
    return


def criar_conta(cliente):
    conta = ContaCorrente.nova_conta(cliente, len(cliente.contas) + 1)

    if conta is not None:
        print("Conta criada com sucesso!")
        return conta
    print("Desculpe, não foi possível criar a conta.")


def escolher_conta(cliente) -> ContaCorrente | None:
    nro_conta = int(input("Nº da conta: "))

    for conta in cliente.contas:
        if nro_conta == conta.numero:
            print("A conta foi acessada com sucesso!")
            return conta

    print("Não foi possível acessar uma conta com esse número.")
    return
