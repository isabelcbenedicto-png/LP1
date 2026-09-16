minutos = int(input("Digite a quantidade de minutos utilizados: "))

if minutos <= 100:
    total = minutos * 0.25
elif minutos <= 300:
    total = minutos * 0.20
elif minutos <= 500:
    total = minutos * 0.15
else:
    total = minutos * 0.10

print(f"Valor a pagar: R$ {total:.2f}")