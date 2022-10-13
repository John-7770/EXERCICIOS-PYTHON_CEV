multiplos = 0

for i in range(1,500+1, 2):
    if i % 3 == 0:
        print(i)
        multiplos += i
        print(multiplos)