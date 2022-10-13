from random import randint
from time import sleep
print('coloque um numero e o computador ira \nfalar se foi isso que ele pensou')
resul = randint(1,5)
num = int(input('pense em um numero de 1 a 5: '))
print('PROCESSANDO...')
sleep(5)
if num == resul:
	print('voce ganhou!!! o numero era {}'.format(resul))
else:
	print('eu ganhei!!! o numero era {}'.format(resul))