from transacao import Deposito, Saque


class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self) -> list:
        return self._contas

    def realizar_transacao(self, conta, transacao):
        if not conta in self._contas:
            print("Conta inválida")
            return

        if isinstance(transacao, Deposito):
            if conta.depositar(transacao.valor):
                transacao.registrar(conta=conta)

        elif isinstance(transacao, Saque):
            if conta.sacar(transacao.valor):
                transacao.registrar(conta)
        else:
            print("Transação inválida")

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def __str__(self):
        return self.__dict__


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, endereco: str):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._numero_saques = 0
        super().__init__(endereco)

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def numero_saques(self) -> int:
        return self._numero_saques

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self._cpf}>"
