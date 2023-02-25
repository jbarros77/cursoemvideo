salário = float(input('Digite o salário: R$'))
novo = salário + (salário * 15 / 100)
print('Seu salário teve 15% de aumento, e agora passa a ser R${:.2f}'.format(novo))