dis = int(input('quantos km levara sua viagem?'))
if dis < 200:
	print('voce tera que pagar R${:.2f}'.format(0.50*dis))
else:
	print('voce tera que pagar R${:.2f}'.format(0.45*dis))