larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg * alt
print('Sua parede tem {} x {} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Vc precisará de {}l de tinta para pintar a parede.'.format(tinta))

#cada litro de tinta pinta 2m de parede.