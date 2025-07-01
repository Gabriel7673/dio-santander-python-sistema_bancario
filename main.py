from operacoes import depositar, sacar, exibirExtrato
from cadastramento import cadastrar_usuario, criar_conta

extrato = ""
saldo = 0
numero_saques = 0

menu = """

Opções
(1) Depositar
(2) Sacar
(3) Extrato
(4) Cadastrar Cliente
(5) Cadastrar Conta
(0) Sair
=> """

while True:
    opcao = input(menu)
    print()

    try:
        if opcao == "1":
            extrato, saldo = depositar(extrato, saldo)
        elif opcao == "2":
            extrato, saldo, numero_saques = sacar(
                saldo=saldo, extrato=extrato, numero_saques=numero_saques)
        elif opcao == "3":
            exibirExtrato(saldo, extrato=extrato)
        elif opcao == "4":
            print(cadastrar_usuario())
        elif opcao == "5":
            print(criar_conta())
        elif opcao == "0":
            print("Encerrando")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    except TypeError:
        continue

