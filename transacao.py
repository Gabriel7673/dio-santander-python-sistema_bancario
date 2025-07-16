from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):

    @abstractmethod
    def registrar(conta):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
        self._data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def data(self):
        return self._data_hora

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f'{self.__class__.__name__} de R${self._valor:.2f} \t {self._data_hora}'

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
        self._data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def data(self):
        return self._data_hora

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f'{self.__class__.__name__} de R${self._valor:.2f} \t {self._data_hora}'