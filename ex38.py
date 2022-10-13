n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))

l1 = [n1, n2]

if n1 == n2:
    print("ambos sao iguais ")
    
if n1 != n2:
    print("o numero menor é {}".format(min(l1)))
    print("o numero maior é {}".format(max(l1)))

