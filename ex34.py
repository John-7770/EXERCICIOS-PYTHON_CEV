s = float(input('salario do funcionario R$'))
dd = s + (s * 15 / 100)
dc = s + (s * 10 / 100)
if s <= 1250:
	print('o valor do salario de R${:.0f} ficara R${:.2f} com 10% de aumento'.format(s, dc))
else:
	print('o valor do salario de R${:.0f} ficara R${:.2f} com 15% de aumento'.format(s, dd))