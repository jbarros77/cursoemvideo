preço = float(input('Qual o preço do produto: R$'))
novo = preço - (preço * 5 / 100)
print('O produto custava {:.2f} e agora com desconto de 5% ficou por {:.2f}.'.format(preço, novo))