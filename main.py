from operacoes import depositar, sacar, exibirExtrato

menu = """

Opções
(1) Depositar
(2) Sacar
(3) Extrato
(0) Sair
=> """

while True:
    opcao = input(menu)
    print()

    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        exibirExtrato()
    elif opcao == "0":
        print("Encerrando")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

