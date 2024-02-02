def calcular_cagr(inicial, final, periodos):
    cagr = (final / inicial) ** (1 / periodos) - 1
    return cagr

inversion_inicial = 10000
inversion_final = 15000
periodos = 3

tasa_cagr = calcular_cagr(inversion_inicial, inversion_final, periodos)

print(f"La tasa de crecimiento anual compuesta (CAGR) es: {tasa_cagr:.2%}")