def alternar_maiusculas(texto):
    resultado = ""
    for i in range(len(texto)):
        if i % 2 ==0:
            resultado += texto[i].upper()
        else:
            resultado += texto[i].lower()
    return resultado