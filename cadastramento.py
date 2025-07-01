from utils import validar_usuario, validar_conta

usuarios = []
contas = []
NUMERO_AGENCIA = '0001'

def cadastrar_usuario():
    print("Seja bem vindo! Por favor digite seus dados:")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    
    valida, msg = validar_usuario(usuarios, cpf)  
    
    
    if valida:
        usuario = (nome, data_nascimento, cpf, endereco,)
        usuarios.append(usuario)
        
    return msg
    

def criar_conta():
    
    cpf = input('CPF do cliente: ')
    
    valida, msg = validar_conta(usuarios, cpf)
    
    if valida:
        conta = (NUMERO_AGENCIA, len(contas)+1, cpf,)
        contas.append(conta)
    
    return msg