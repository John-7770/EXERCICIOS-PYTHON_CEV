print('ANALISANDOR  DE TRIANGULO')
print('-='*20)
c1 = float(input('primeiro segmento: '))
c2 = float(input('segundo segmento: '))
c3 = float(input('terceiro segmento: '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
	print('analisando os parametros eles formam um triangulo'.upper())
	if c1 == c2 and c1 == c3:
		print("\033[0;31;mEQUILATERO")
	elif c1 == c2 or c1 == c3:
		print("\033[0;31;mISOCELES")
	else:
		print("\033[0;31;mESCALENO")
else:
	print('analisando os parametros eles nao formam um triangulo'.upper())
