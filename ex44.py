import os
import time

print("\033[0;33;mbem vindo a Loja Glang")
time.sleep(3)
os.system("cls")


n = int(input("preço do produto: "))

print("[1] \033[0;32;ma vista DINHEIRO/CHEQUE 10 % de desconto\n\033[0;32;m[2]a vista no cartao 5 % de desconto\n\033[0;33;m[3] em ate 2x no cartao\n\033[0;33;m[4]3x ou mais")

rest = int(input("\033[0;31;m>> "))

if rest == 1:
    n = n - (n * 10 / 100)
    print("voce tera que pagar R${} com 10 % de desconto".format(n))
elif rest == 2:
    n = n - (n * 5 / 100)
    print("voce tera que pagar R${} com 5 % de desconto".format(n))
elif rest == 3:
    n = n / 2
    print("voce ira pagar R${} em 2X no cartao")
elif rest == 4:
    mais = int(input("em quantas vezes deseja pagar no cartao? "))
    mais1 = n / mais
    print("em {}X no cartao voce ira pagar R${:.2f}".format(mais, mais1))