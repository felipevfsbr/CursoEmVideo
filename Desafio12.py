valor = float(input('Qual é o preco do produto?: R$'))
d = float(input('Qual a porcentagem de desconto desse produto?:'))


print('O produto que custava R${}, na promocao de desconto de {} vai custar R${}'.format(valor, d, valor-(valor*d/100)))
