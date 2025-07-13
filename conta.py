from historico import Historico

class Conta:
    
    AGENCIA = "0001"
    nro_conta = 1

    def __init__(self, saldo: float = 0, numero: int = None, 
                 cliente = None, historico=Historico()):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._historico = historico

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente=cliente, numero=numero)

    def sacar(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        pass

class ContaCorrente(Conta):
    def __init__(self, limite: float = 500, limite_saques: int = 3, 
                 numero: int = None, cliente = None, 
                 saldo: float = 0, historico = Historico()):
        
        super().__init__(numero=numero, cliente=cliente, saldo=saldo, 
                         historico=historico)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        self._saldo -= valor
        return True 
        # TODO: fazer validações

    def depositar(self, valor: float) -> bool:
        self._saldo += valor
        return True

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'