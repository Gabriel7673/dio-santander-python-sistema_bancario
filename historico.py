from datetime import datetime

from transacao import Saque


class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or isinstance(transacao, tipo_transacao):
                yield transacao

    def saques_do_dia(self):
        data_atual = datetime.now().date()
        transacoes = 0
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao.data, "%d/%m/%Y %H:%M:%S"
            ).date()
            print(data_atual, data_transacao)
            if data_atual == data_transacao and isinstance(transacao, Saque):
                transacoes += 1
        return transacoes

    def __str__(self):
        lista = "\n".join(str(t) for t in self._transacoes)
        return f"{self.__class__.__name__}:\n{lista}"
