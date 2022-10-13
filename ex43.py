print("bem vindo ao calculador de IMC")

altura = float(input("sua altura: "))
peso = float(input("seu peso: "))
calculo = peso / (altura * altura)

if calculo < 18.6:
    print("\033[0;31;mvoce esta abaixo do peso")
elif calculo > 18.5 and calculo < 25:
    print("\033[0;32;mvoce esta com um peso ideal")
elif calculo > 25 and calculo < 31:
    print("sobrepeso")
elif calculo > 30 and calculo < 41:
    print("obesidade")
elif calculo > 40:
    print("obesidade morbida    '")