import random


m = random.randint(1,101)
print("bem vindo ao jogo do jokenpô")


n = int(input("\nescolha um numero de 1 a 100: "))

if n == m:
    print("parabens o numero era {}".format(m))
elif n != m:
    print("que pena o numero era {}".format(m))
    if n > 101:
        print("\nnumero muito alto pense menos")