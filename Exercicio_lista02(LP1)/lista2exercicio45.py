salario = float(input("Digite o salário: R$ "))
tempo = float(input("Digite o tempo de empresa (em anos): "))

if salario < 2000:
    if tempo >= 5:
        print("Elegível a reajuste.")