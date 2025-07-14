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