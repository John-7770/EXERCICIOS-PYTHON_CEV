from math import trunc
real = float(input('digite um numero real:'))
porçao = trunc(real)
print ('o numero REAL {:.3f} tem a porçao inteira {}'.format(real, porçao))