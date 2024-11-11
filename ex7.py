def conta_vogais(texto):
    contador = 0
    i = 0
    while i < len(texto):
        if texto[i] in "aeiouAEIOU":
            contador +=1
        i +=1
    return contador 