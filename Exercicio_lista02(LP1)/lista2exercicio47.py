n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2:
    if n1 > n3:
        maior = n1
    else:
        maior = n3
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3

print(f"O maior número é: {maior}")