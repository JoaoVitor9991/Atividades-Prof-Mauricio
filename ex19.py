def apaga_vogais(s):
        resultado = ""
        for caracter in s:
                if caracter not in "aeiouAEIOU":
                        resultado += caracter
        return resultado
    
