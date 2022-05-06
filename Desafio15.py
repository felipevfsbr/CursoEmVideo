# author : Néris

dias = int(input('Quantos dias o carro foi alugado?:'))
km = float(input('quantos km o carro percorreu?'))



print('O carro foi utilizado por {} dias e percorreu {}km, logo o valor foi R${:.2f}'.format(dias, km, (dias*60)+(km*0.15)))
