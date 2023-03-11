distância = float(input('Informe a distância da sua viagem: '))
print('Sua viagem vai ser de {}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('Vc vai pagar R$ {:.2f} na passagem'.format(preço))

'''preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(' O preço da viagem será R${:.2f}'.format(preço))
(outra forma de resolver)'''