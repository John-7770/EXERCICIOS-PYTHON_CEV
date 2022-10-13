print("bem vindo ao construtor de tabuada".title())

n = int(input("qual tabuada quer? ".title()))

for i in range(0,11):
    print("{} X {} = {}".format(n, i, n*i))
