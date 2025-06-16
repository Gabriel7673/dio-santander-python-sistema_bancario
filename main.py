menu = """

Opções
(1) Depositar
(2) Sacar
(3) Extrato
(0) Sair
=> """

extrato = ""
saldo = 0
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

def converteStrParaFloat(valorStr: str) -> float:
    try:
        valor = float(valorStr)
        return valor
    except ValueError:
        print("Valor inválido.")

while True:
    opcao = input(menu)
    print()

    if opcao == "1":
        print("Depósito:")
        valorStr = input("Valor a depositar: ")
        valor = converteStrParaFloat(valorStr)
        
        if valor is None: continue

        if valor > 0:
            saldo += valor
            extrato += f"+ R${valor:.2f}\n"
        else:
            print("Valores positivos apenas.")
        

    
    elif opcao == "2":
        print("Saque:")
        valorStr = input("Valor a sacar: ")
        valor = converteStrParaFloat(valorStr)

        if valor is None: continue

        if valor > 500:
            print(f"O limite de saque é de R${LIMITE:.2f}.")
        else:
            if numero_saques >= LIMITE_SAQUES:
                print(f"O limite de saques diários é {LIMITE_SAQUES} vezes.")
            else:
                if saldo < valor:
                    print("Saldo insuficiente.")
                else:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"- R${valor:.2f}\n"

    elif opcao == "3":
        print("Extrato:")
        if extrato:
            print(f"{extrato}\nSaldo atual: R${saldo:.2f}")
        else:
            print("Extrato está vazio.")

    elif opcao == "0":
        print("Encerrando")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

