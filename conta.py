class Conta:

    AGENCIA = "0001"


    def __init__(self, numero, cliente, saldo = 0, historico=[]):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo
    
    def nova_conta(cliente, numero):
        pass

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques, numero, cliente, saldo=0, historico=[]):
        super().__init__(numero, cliente, saldo, historico)
        self._limite = limite
        self._limite_saques = limite_saques
