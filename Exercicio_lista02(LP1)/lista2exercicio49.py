temp = float(input("Digite a temperatura (°C): "))
umidade = float(input("Digite a umidade do ar (%): "))

if temp > 30:
    if umidade < 30:
        print("Alerta de incêndio!")
    else:
        print("Calor, mas sem risco de incêndio.")