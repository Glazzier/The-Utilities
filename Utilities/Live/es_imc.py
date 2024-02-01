def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc, edad):
    if edad < 18:
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidad clase 1"
        elif 35 <= imc < 39.9:
            return "Obesidad clase 2"
        else:
            return "Obesidad clase 3"
    else:
        if imc < 22:
            return "Bajo peso"
        elif 22 <= imc < 27:
            return "Peso normal"
        elif 27 <= imc < 32:
            return "Sobrepeso"
        elif 32 <= imc < 37:
            return "Obesidad clase 1"
        elif 37 <= imc < 42:
            return "Obesidad clase 2"
        else:
            return "Obesidad clase 3"

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
edad = int(input("Ingresa tu edad: "))

imc = calcular_imc(peso, altura)

clasificacion = clasificar_imc(imc, edad)

print(f"\nTu IMC es: {imc:.2f}")
print(f"Clasificación: {clasificacion}")
print(f"Edad: {edad} años")
