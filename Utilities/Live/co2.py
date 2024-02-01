def calcular_huella_carbono():
    print("Calculadora de Huella de Carbono")
    
    distancia_coche = float(input("Ingresa la distancia recorrida en coche en kilómetros: "))
    consumo_coche = float(input("Ingresa el consumo de combustible del coche en litros por kilómetro: "))
    
    electricidad_consumida = float(input("Ingresa la cantidad de electricidad consumida en kilovatios por hora: "))
    
    factor_emision_coche = 2.3
    factor_emision_electricidad = 0.6
    
    huella_coche = distancia_coche * consumo_coche * factor_emision_coche
    huella_electricidad = electricidad_consumida * factor_emision_electricidad
    
    huella_total = huella_coche + huella_electricidad
    
    print("\nResultados:")
    print(f"Huella de carbono por coche: {huella_coche} kg de CO2")
    print(f"Huella de carbono por electricidad: {huella_electricidad} kg de CO2")
    print(f"Huella de carbono total: {huella_total} kg de CO2")

calcular_huella_carbono()