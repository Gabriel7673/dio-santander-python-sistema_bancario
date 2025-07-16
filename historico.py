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


    def __str__(self):
        lista = "\n".join(str(t) for t in self._transacoes)
        return f'{self.__class__.__name__}:\n{lista}'
    
    