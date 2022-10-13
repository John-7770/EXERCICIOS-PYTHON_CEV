from math import hypot 
co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hypot = hypot(co, ca)
print ('a hipotenusa do cateto è {:.2f}.'.format(hypot))