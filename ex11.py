alt = float(input('qual a altura da parede:'))
lar = float(input('qual a largura da  parede:'))
area = alt * lar
print ('sua parede tem a dimensao de {}x{} e sua area è de {}m²'.format(alt, lar, area))
tinta = area / 2
print ('para pintar essa parede voce precisara de {}L de tinta'.format(tinta))