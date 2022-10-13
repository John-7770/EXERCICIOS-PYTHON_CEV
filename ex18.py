import math
angulo= float(input('qual o valor do angulo:'))
seno = math.sin(math.radians(angulo))
print ('o angulo {} tem o SENO {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print ('o angulo {} tem o cosseno {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print ('o angulo {} tem o tangente {:.2f}'.format(angulo, cosseno))