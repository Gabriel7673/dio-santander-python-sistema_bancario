from models.transacao import Deposito, Saque


class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self) -> str:
        return self._endereco

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
    def data_nascimento(self) -> str:
        return self._data_nascimento

    @property
    def numero_saques(self) -> int:
        return self._numero_saques

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self._cpf}>"


class PessoaJuridica(Cliente):
    def __init__(self, cnpj: str, nome_social: str, razao_social: str, endereco: str):
        self._cnpj = cnpj
        self._nome_social = nome_social
        self._razao_social = razao_social
        self._numero_saques = 0
        super().__init__(endereco)

    @property
    def cnpj(self) -> str:
        return self._cnpj

    @property
    def nome_social(self) -> str:
        return self._nome_social

    @property
    def razao_social(self) -> str:
        return self._razao_social

    @property
    def numero_saques(self) -> int:
        return self._numero_saques

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self._cnpj}>"
