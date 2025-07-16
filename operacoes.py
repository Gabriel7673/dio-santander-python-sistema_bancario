from utils import converteStrParaFloat, log_transacao
from transacao import Deposito, Saque

@log_transacao
def depositar(cliente, conta):
    valorStr = input("Valor a depositar: ")
    valor = converteStrParaFloat(valorStr)
        
    if valor is None: return

    if valor > 0:
        cliente.realizar_transacao(conta, Deposito(valor))
    else:
        print("São aceitos valores positivos apenas.")

@log_transacao
def sacar(cliente, conta):
    valorStr = input("Valor a sacar: ")
    valor = converteStrParaFloat(valorStr)

    if valor is None: return

    numero_saques = conta.historico.saques_do_dia()

    if valor > conta.limite:
        print(f"O limite de saque é de R${conta.limite:.2f}.")
    elif valor <= 0:
        print("São aceitos valores positivos apenas.")
    elif numero_saques >= conta.limite_saques:
        print(f"O limite de saques diários é {conta.limite_saques} vezes.")
    elif conta.saldo < valor:
        print("Saldo insuficiente.")
    else:
        cliente.realizar_transacao(conta, Saque(valor))

@log_transacao
def exibir_historico(conta):
    historico = conta.historico
    if not historico.transacoes:
        print("Nenhuma transação realizada")
        return
    menu_filtro = '''
Filtrar histórico por:
(1) Depósitos
(2) Saques
(3) Sem restrições
=> '''
    opcao = input(menu_filtro)
    filtro = None
    match opcao:
        case "1":
            filtro = Deposito
        case "2": 
            filtro = Saque
        case "3":
            filtro = None
    if filtro is None:
        print(historico)
    else:
        lista = []
        for t in historico.gerar_relatorio(filtro):
            lista.append(str(t))
        print(f'{historico.__class__.__name__}:\n{"\n".join(lista)}')


    print("-" * 25)
    print(f'Saldo atual de R${conta.saldo:.2f}')