texto = input("Digite uma palavra para inverter: ")

def inverter(texto):
    return texto[::-1]

texto_invertido = inverter(texto)

print(texto_invertido)