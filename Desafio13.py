# Author: Néris

valor = float(input('Qual é o salario do funcionario?: R$'))
d = float(input('Qual a porcentagem de aumento de salario?:'))


print('O Salario que era de R${}, com o aumento de {} vai para R${}'.format(valor, d, valor+(valor*d/100)))
