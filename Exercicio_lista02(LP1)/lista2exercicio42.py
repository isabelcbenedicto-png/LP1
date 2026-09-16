nota = float(input("Digite a nota final: "))
faltas = int(input("Digite o número de faltas: "))

if faltas > 15:
    print("Reprovado por falta.")
elif nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D")