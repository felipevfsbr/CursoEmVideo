# author:Néris
import math

angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))


print('O Seno vai medir {:.2f}'
      ' A tangente vai medir {:.2f}'
      ' O cosseno vai medir {:.2f}'.format(seno, tan, cos))
