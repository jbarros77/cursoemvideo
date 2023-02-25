co = float(input('Comprimento do cateto oposto mede: '))
ca = float(input('Comprimento do cateto adjacente mede: '))
hi =(co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

'''Pode importar o math e fazer o calcúlo diferente usando: 
hi = math.hypot(co, ca)'''