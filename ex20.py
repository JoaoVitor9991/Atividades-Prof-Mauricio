def troca_vogais(s, nova_letra):
    vogais = "aeiouAEIOU"
    nova_string =""

    for i in s:
        if i in vogais:
            nova_string += nova_letra
        else:
            nova_string +=1

    return nova_string
