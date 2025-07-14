from utils import validar_usuario, validar_para_conta
from cliente import PessoaFisica
from conta import ContaCorrente

usuarios = []

def cadastrar_usuario():
    print("Seja bem vindo! Por favor digite seus dados:")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    
    valida, msg = validar_usuario(usuarios, cpf)  
    
    
    if valida:
        usuario = PessoaFisica(cpf, nome, data_nascimento, endereco,)
        usuarios.append(usuario)
        
    return msg
    
def entrar_usuario():
    cpf = input("CPF: ")
    
    cpf_valido, _ = validar_para_conta(usuarios, cpf)

    if cpf_valido:
        for usuario in usuarios:
            if cpf == usuario.cpf:
                return usuario
    print("CPF não registrado.")
    return 

def criar_conta(cliente):
    conta = ContaCorrente.nova_conta(cliente, len(cliente.contas)+1)

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