from operacoes import depositar, sacar, exibir_historico
from cadastramento import cadastrar_usuario, criar_conta, entrar_usuario, escolher_conta
from conta import ContaIterador

menu_inicial = """

Opções:
(1) Efetuar Login
(2) Cadastrar Cliente
(0) Encerrar
=> """

menu_operacoes = """
(1) Depositar
(2) Sacar
(3) Histórico da Conta
(4) Cadastrar Conta
(5) Trocar Conta
(6) Listar Contas
(0) Sair
=> """


while True:
    opcao = input(menu_inicial)
    print()

    try:
        if opcao == "1":
            cliente = entrar_usuario()

            if cliente.contas == []:
                conta = criar_conta(cliente)
                cliente.adicionar_conta(conta)
            else:
                conta = cliente.contas[0]
            while True:
                print(f'\nAgência {conta.AGENCIA} - Conta {conta.numero}')
                opcao2 = input(menu_operacoes)
                print()

                try:                    
                    if opcao2 == "1":
                        depositar(cliente, conta)
                    elif opcao2 == "2":
                        sacar(cliente, conta)
                    elif opcao2 == "3":
                        exibir_historico(conta)
                    elif opcao2 == "4":
                        conta = criar_conta(cliente)
                        cliente.adicionar_conta(conta)
                    elif opcao2 == "5":
                        conta = escolher_conta(cliente)
                    elif opcao2 == "6":
                        for c in ContaIterador(cliente.contas):
                           print(c)
                    elif opcao2 == "0":
                        print("Encerrando")
                        break
                    else:
                        print("Opção inválida. Por favor, escolha uma opção válida.")
                except TypeError:
                    continue
        elif opcao == "2":
            print(cadastrar_usuario())
        elif opcao == "0":
            print("Encerrando")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    except TypeError:
        continue