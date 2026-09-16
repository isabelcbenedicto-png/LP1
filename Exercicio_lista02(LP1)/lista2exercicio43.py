valor = float(input("Digite o valor da compra: R$ "))

if valor <= 50:
    valor_final = valor
elif valor <= 200:
    valor_final = valor * 0.95
elif valor <= 500:
    valor_final = valor * 0.90
else:
    valor_final = valor * 0.85

print(f"Valor final com desconto: R$ {valor_final:.2f}")