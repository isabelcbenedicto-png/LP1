valor = float(input("Digite o valor da compra: R$ "))
forma_pagamento = input("Forma de pagamento ('dinheiro' ou 'cartao'): ").strip().lower()

if forma_pagamento == "dinheiro":
    valor_final = valor * 0.90
    print(f"Valor final com 10% de desconto: R$ {valor_final:.2f}")
elif forma_pagamento == "cartao":
    parcelas = int(input("Digite o número de parcelas: "))
    if parcelas > 3:
        print("Haverá juros de 2% ao mês.")
    else:
        print("Pagamento será sem juros.")
    print(f"Valor da compra: R$ {valor:.2f}")