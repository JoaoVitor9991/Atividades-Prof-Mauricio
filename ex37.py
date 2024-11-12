def e_armstrong(n):
    num_str = str(n)
    num_digitos = len(num_str)
    soma = 0
    for digito in num_str:
        soma += int(digito) ** num_digitos

    return soma == n