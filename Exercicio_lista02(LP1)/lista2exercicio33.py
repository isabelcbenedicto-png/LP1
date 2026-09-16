valor = float(input("Digite o valor da compra: R$ "))

if valor > 100:
    valor_final = valor * 0.90
    print(f"Desconto de 10% aplicado! Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor final: R$ {valor:.2f}")