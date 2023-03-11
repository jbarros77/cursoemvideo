cidade = input('Digite o nome da cidade: ')
if cidade.lower().lstrip().find('santo') == 0:
    print('{} começa com Santo!'.format(cidade))
else:
    print('{} não começa com Santo!'.format(cidade))


'''OUTRA FORMA PARA SOLUCIONAR

cid = str(input('Digite a sua cidade: '))
print(cid[:5].upper() == 'SANTO')'''






