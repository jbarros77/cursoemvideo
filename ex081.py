valores = []
while True:
    valores.append(int(input(f'Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-*-'*30)
print(f'Vc digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores decrescentes foram {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado!')
