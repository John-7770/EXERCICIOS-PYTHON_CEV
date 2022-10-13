import time
import os

print("bem vindo a confederaçao de nataçao")
time.sleep(0)
os.system("cls")

nome = str(input("digite seu nome: "))
idade = int(input("digite sua idade: "))

if idade < 10:
    print("\033[0;33;mvoce ira participar da categoria MIRIM")
elif idade > 9 and idade < 15:
    print("\033[0;33;mvoce ira participar da categoria INFANTIL")
elif idade > 14 and idade < 20:
    print("\033[0;33;mvoce ira participar da categoria JUNIOR")
elif idade > 19 and idade < 21:
    print("\033[0;33;mvoce ira participar da categoria SENIOR")
else:
    print("\033[0;33;mvoce ira participar da categoria MASTER")