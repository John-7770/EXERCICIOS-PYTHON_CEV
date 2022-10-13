##  soluçao simples 1

cont = 0
soma =  0

for num in range(0,6):
   n = int(input(">> "))
   if n % 2 == 0:
       soma += n
       cont += 1
print("{} numeros sao pares e o total sao {}".format(cont, soma))


############# soluçao 2

#for num in range(0,6):
 #   n = int(input(">> "))
 #   nm = "{}".format(n/2)
 #   so = nm[-1]
 #   if int(so) == 0:
 #       soma += n
 #       cont += 1
 #       print(so)

#print("{} numeros sao pares e o total de tudo é {}".title().format(cont, soma))
























##soluçao 2 completa

#cont = 0
#soma =  0

#or num in range(0,6):
#   n = int(input(">> "))
#   if n % 2 == 0:
#       soma += n
#       cont += 1

#print("{} nu