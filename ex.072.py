#crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso de zero até vinte.
#seu programa deverá ler um número pelo teclado (entre 0 e 20)
#e mostra-lo por extenso:

cont = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
        'doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
        num = int(input(f'Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
                break
        print('Tente outra vez: ', end='')
print(f'Você digitou o número {cont[num]}')