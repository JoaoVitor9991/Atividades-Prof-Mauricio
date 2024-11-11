def capitalize_palavra(texto):
    texto = texto.split()
    for i in range(len(texto)):
        texto[i] = texto[i].capitalize()
    return " ".join(texto)