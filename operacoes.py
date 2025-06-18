from utils import converteStrParaFloat

extrato = ""
saldo = 0
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    
    print("Depósito:")
    valorStr = input("Valor a depositar: ")
    valor = converteStrParaFloat(valorStr)
        
    if valor is None: return

    if valor > 0:
        saldo += valor
        extrato += f"+ R${valor:.2f}\n"
    else:
        print("São aceitos valores positivos apenas.")

def sacar():
    global saldo, numero_saques, extrato

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

def exibirExtrato():
    print("Extrato:")
    if extrato:
        print(f"{extrato}\nSaldo atual: R${saldo:.2f}")
    else:
        print("Extrato está vazio.")