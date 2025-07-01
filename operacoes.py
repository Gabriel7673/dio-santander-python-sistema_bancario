from utils import converteStrParaFloat

LIMITE = 500
LIMITE_SAQUES = 3

def depositar(extrato, saldo, /):
    
    print("Depósito:")
    valorStr = input("Valor a depositar: ")
    valor = converteStrParaFloat(valorStr)
        
    if valor is None: return

    if valor > 0:
        saldo += valor
        extrato += f"+ R${valor:.2f}\n"
        return extrato, saldo
    else:
        print("São aceitos valores positivos apenas.")

def sacar(*, extrato, saldo, numero_saques):

    print("Saque:")
    valorStr = input("Valor a sacar: ")
    valor = converteStrParaFloat(valorStr)

    if valor is None: return

    if valor > 500:
        print(f"O limite de saque é de R${LIMITE:.2f}.")
    elif valor <= 0:
        print("São aceitos valores positivos apenas.")
    elif numero_saques >= LIMITE_SAQUES:
        print(f"O limite de saques diários é {LIMITE_SAQUES} vezes.")
    elif saldo < valor:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"- R${valor:.2f}\n"
        return extrato, saldo, numero_saques

def exibirExtrato(saldo, /, *, extrato):
    print("Extrato:")
    if extrato:
        print(f"{extrato}\nSaldo atual: R${saldo:.2f}")
    else:
        print("Extrato está vazio.")