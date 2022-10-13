n = int(input("digite sua primeira nota: "))
n1 = int(input("digite sua segunda nota: "))

notaF = float((n + n1)/ 2)

if notaF < 5.0:
    print("\033[0;31;mvoce foi reprovado sua media é de {}".format(notaF))
elif notaF > 4.0 and notaF < 7.0:
    print("\033[0;32;mvoce esta de recuperaçao sua media é de {}".format(notaF))
elif notaF > 7.0:
    print("\033[0;33;mvoce passou sua media é de {}".format(notaF))