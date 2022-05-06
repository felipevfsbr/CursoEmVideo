# author: Néris

nome = str(input('Digite Seu Nome Completo:')).strip()
nome1 = nome.split()
print('Analisando seu nome...')
print('Seu nome em letras Maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras Minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} Caracteres'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} caracteres'.format(nome1[0], len(nome1[0])))
