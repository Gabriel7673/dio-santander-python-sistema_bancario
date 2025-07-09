class Cliente:
    def __init__(self, endereco, contas=[]):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao():
        pass

    def adicionar_conta():
        pass

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas=[]):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento