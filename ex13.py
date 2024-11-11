def conta_letras(s, letrao):
    contador = 0
    for caracter in s:
        if caracter == letrao:
            contador+=1
    return contador

