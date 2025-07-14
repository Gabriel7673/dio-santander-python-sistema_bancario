from abc import ABC, abstractmethod

class Transacao(ABC):

    @abstractmethod
    def registrar(conta):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        super().__init__()
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f'{self.__class__.__name__} de R${self._valor:.2f}'

class Saque(Transacao):
    def __init__(self, valor: float):
        super().__init__()
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f'{self.__class__.__name__} de R${self._valor:.2f}'