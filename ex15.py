dias = float (input('quantos dias o carro foi alugado:'))
km = float(input('quantos km o carro rodou?'))
total = (dias * 60) + (km * 0.15)
print ('o preço a pagar pelo aluguel è de {:.2f}'.format(total))