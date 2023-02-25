n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('E o triplo de {} vale {}. \nE a raiz quadrada de {} é {:.2f}.'.format(n, t, n, r))

#posso formatar a raiz quadrada usando {:.2f} e tmb usando pow(n, (1/2)) no lugar da variavel r