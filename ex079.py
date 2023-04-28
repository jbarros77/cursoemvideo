# Crie um programa onde o usuário possa digitar vários
# valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

numeros = []

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    if numero not in numeros:
        numeros.append(numero)

numeros.sort()

print("Valores únicos digitados, em ordem crescente:")
for numero in numeros:
    print(numero)









