def converteStrParaFloat(valorStr: str) -> float:
    try:
        valor = float(valorStr)
        return valor
    except ValueError:
        print("Valor inválido.")
