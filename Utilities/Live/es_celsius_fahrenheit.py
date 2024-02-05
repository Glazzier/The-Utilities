def convertir_temperatura(temperatura, escala):
    try:
        temperatura = float(temperatura)
        if escala.upper() == 'C':
            resultado = (temperatura * 9/5) + 32
            return resultado, 'F'
        elif escala.upper() == 'F':
            resultado = (temperatura - 32) * 5/9
            return resultado, 'C'
        else:
            return "Escala no válida. Ingresa 'C' o 'F'", None
    except ValueError:
        return "Error: Ingresa una temperatura válida como número", None

try:
    temperatura_ingresada = input("Ingresa la temperatura: ")
    escala_ingresada = input("Ingresa la escala (C o F): ")

    resultado, nueva_escala = convertir_temperatura(temperatura_ingresada, escala_ingresada)

    if nueva_escala:
        print(f"{temperatura_ingresada}°{escala_ingresada} es igual a {resultado:.2f}°{nueva_escala}")
    else:
        print(resultado)

except Exception as e:
    print(f"Error: {e}")
