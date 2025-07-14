from utils import converteStrParaFloat
from transacao import Deposito, Saque

def depositar(cliente, conta):
    
    print("Depósito:")
    valorStr = input("Valor a depositar: ")
    valor = converteStrParaFloat(valorStr)
        
    if valor is None: return

    if valor > 0:
        cliente.realizar_transacao(conta, Deposito(valor))
    else:
        print("São aceitos valores positivos apenas.")

def sacar(cliente, conta):

    print("Saque:")
    valorStr = input("Valor a sacar: ")
    valor = converteStrParaFloat(valorStr)

    if valor is None: return

    if valor > conta.limite:
        print(f"O limite de saque é de R${conta.limite:.2f}.")
    elif valor <= 0:
        print("São aceitos valores positivos apenas.")
    elif cliente.numero_saques >= conta.limite_saques:
        print(f"O limite de saques diários é {conta.limite_saques} vezes.")
    elif conta.saldo < valor:
        print("Saldo insuficiente.")
    else:
        cliente.realizar_transacao(conta, Saque(valor))
        cliente.contar_saque()

def exibirHistorico(conta):
    print(conta.historico)
    print(f'Saldo atual de R${conta.saldo:.2f}')