idade = int(input("Digite a idade: "))
sexo = input("Digite o sexo (M/F): ").upper()

if sexo == 'M':
    if idade >= 18:
        print("Apto ao serviço militar.")