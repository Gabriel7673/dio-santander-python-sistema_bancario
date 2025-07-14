from historico import Historico

class Conta:
    
    AGENCIA = "0001"

    def __init__(self, numero: int = None, 
                 cliente = None):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._historico = Historico()

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> int:
        return self._numero
    
    @property
    def historico(self) -> Historico:
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente=cliente, numero=numero)

    def sacar(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        pass

class ContaCorrente(Conta):
    def __init__(self, limite: float = 500, limite_saques: int = 3, 
                 numero: int = None, cliente = None):
        
        super().__init__(numero=numero, cliente=cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self) -> float:
        return self._limite
    
    @property
    def limite_saques(self) -> int:
        return self._limite_saques

    def sacar(self, valor: float) -> bool:
        self._saldo -= valor
        return True 

    def depositar(self, valor: float) -> bool:
        self._saldo += valor
        return True

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'