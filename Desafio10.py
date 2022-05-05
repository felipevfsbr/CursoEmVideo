# author:néris

real = float(input('Digite quanto de dinheiro voce tem: R$'))
dolar = float(real / 4.90)

print('com o valor R${:.2f}, é possivel comprar U${:.2f}.'.format(real, dolar))
