nome = input("Nome do funcionário: ")
salario = float(input("Salário atual: "))
percentual = float(input("Percentual de aumento (%): "))

aumento = salario * (percentual / 100)
novo_salario = salario + aumento
print("O funcionário " + nome + " terá um novo salário de R$ " + str(novo_salario))
