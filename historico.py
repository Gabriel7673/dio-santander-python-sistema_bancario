class Historico:

    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    def __str__(self):
        if not self._transacoes:
            return "Nenhuma transação realizada"
        lista = "\n".join(str(t) for t in self._transacoes)
        return f'{self.__class__.__name__}:\n{lista}'