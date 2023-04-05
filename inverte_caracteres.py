string = input("Digite uma string:")

caracteres = list(string)

inicio = 0
fim= len(caracteres) -1

while inicio < fim:
    temp = caracteres[inicio]
    caracteres[inicio] = caracteres[fim]
    caracteres[fim] = temp

    inicio +=1
    fim -= 1

string_invertida = ''.join(caracteres)
print("String invertida:", string_invertida)