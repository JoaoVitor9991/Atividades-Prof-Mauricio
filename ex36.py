def e_perfeito(n):
    soma = 0
    for i in range(1 , n):
        if n % i ==0:
            soma += i
    return soma == n

