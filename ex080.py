# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.


lista = []

for i in range(5):
    num = int(input("Digite um número: "))
    if i == 0:
        lista.append(num)
    else:
        for j in range(len(lista)):
            if num <= lista[j]:
                lista.insert(j, num)
                break
            elif j == len(lista)-1:
                lista.append(num)
                break

print("Lista ordenada:", lista)


