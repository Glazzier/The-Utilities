def calcular_propina(cuenta, porcentaje_propina):
    propina = cuenta * (porcentaje_propina / 100)
    return propina

def main():
    monto_cuenta = float(input("Ingrese el monto de la cuenta: $"))
    porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

    propina_calculada = calcular_propina(monto_cuenta, porcentaje_propina)

    print(f"\nMonto de la cuenta: ${monto_cuenta}")
    print(f"Porcentaje de propina: {porcentaje_propina}%")
    print(f"Propina calculada: ${propina_calculada:.2f}")

    total = monto_cuenta + propina_calculada
    print(f"Total a pagar: ${total:.2f}")

main()
