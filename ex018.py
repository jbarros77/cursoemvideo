import math
ângulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem Seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem Cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem Tangente de {:.2f}'.format(ângulo, tangente))