from transacao import Deposito, Saque

class Cliente:
    def __init__(self, endereco: str, contas: list = []):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        if not conta in self._contas:
            print("Conta inválida")
            return
        
        if isinstance(transacao, Deposito):           
            if conta.depositar(transacao._valor):
                transacao.registrar(conta=conta)
            
        elif isinstance(transacao,Saque):
            if conta.sacar(transacao._valor):
                transacao.registrar(conta)
        else:
            print("Transação inválida")

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def __str__(self):
        return self.__dict__

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, 
                 endereco: str, contas: list = []):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco, contas)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'
    







