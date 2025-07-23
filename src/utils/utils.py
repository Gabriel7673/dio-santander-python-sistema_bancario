from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def converteStrParaFloat(valorStr: str) -> float:
    try:
        valor = float(valorStr)
        return valor
    except ValueError:
        print("Valor inválido.")


def validar_usuario(usuarios, cpf):

    if not cpf_eh_numerico(cpf):
        return False, "Somente são aceitos números no CPF."

    if cpf_cadastrado(usuarios, cpf):
        return False, "CPF já cadastrado."

    return True, "Cadastro bem sucedido!"


def validar_para_conta(usuarios, cpf):

    if not cpf_eh_numerico(cpf):
        return False, "Somente são aceitos números no CPF."

    if not cpf_cadastrado(usuarios, cpf):
        return False, "CPF não cadastrado."

    return True, "Cadastro bem sucedido!"


def cpf_eh_numerico(cpf):
    if cpf.isdigit():
        return True


def cpf_cadastrado(usuarios, cpf):
    for u in usuarios:
        if cpf == u.cpf:
            return True


def log_transacao(funcao):
    def wrapp(*args, **kwargs):
        data_hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        print(
            f'{data_hora} -> { \
            " ".join(funcao.__name__.split("_")).capitalize()}'
        )
        resultado = funcao(*args, **kwargs)
        try:
            with open(ROOT_PATH / "log.txt", "a", encoding="utf-8") as file:
                file.write(
                    f"[{data_hora}] Função '{funcao.__name__}' \
executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"
                )
        except IOError as error:
            print(f"Erro ao abrir o arquivo")
        except UnicodeEncodeError as error:
            print(error)

    return wrapp
