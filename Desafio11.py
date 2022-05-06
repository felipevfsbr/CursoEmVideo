#author:néris

A = float(input('Insira a Largura da parede:'))
L = float(input('Insira a Altura da parede:'))
area = (A*L)
tinta= (area/2)

print('Sua parede tem Dimensao {}m x {}m e sua area é de {}m² '
      'para pintar essa parede, voce precisara de {}L de tinta'.format(A, L, area, tinta))
