#tuplas com times de futebol
#a) Os 5 primeiros times.
#b) Os últimos 5 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do sport.

times= ('abc','atletico-go','avaí','botafogo','céara','chapecoense',
        'crb','criciuma',
        'guarani','ituano','juventude','londrina','mirassol','novorizontino',
        'pontepreta','sampaiocorrêa','sport','tombense','vilanova','vitória')

print(times)
print('=-=' * 20)
print(f'Os 5 primeiros na tabela são: {times[0:5]} ')
print('=-=' * 20)
print(f'Os 5 últimos na tabela são: {times[-5:]}')
print('=-=' * 20)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('=-=' * 20)
print(f'O sport está na {times.index("sport")+1}° posição na tabela')

#pq esse +1, pq a contagem em python começa em zero, senão seria 16°posição.
