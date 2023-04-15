salário = float(input('Informe o salário do funcionário: '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print( 'Quem ganhava R${:.2f},passa a receber R${:.2f} agora.'.format(salário, novo))