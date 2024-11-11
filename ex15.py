def ocorrencias_palavras(texto):
    texto = texto.split()
    dicionario= {}
    for palavra in texto:
        if palavra in dicionario:
            dicionario[palavra] +=1
        else:
            dicionario[palavra]= 1
    return dicionario
        
            
        