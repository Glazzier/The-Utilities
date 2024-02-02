import os
import pandas as pd
from datetime import datetime

class HabitosManager:
    def __init__(self, usuario):
        self.usuario = usuario
        self.habitos = pd.DataFrame(columns=['Hábito', 'Completado', 'Última Actualización'])
        self.archivo_excel = f"{usuario}_habitos.xlsx"
        self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.archivo_excel):
            self.habitos = pd.read_excel(self.archivo_excel)

    def guardar_datos(self):
        self.habitos.to_excel(self.archivo_excel, index=False)

    def agregar_habito(self, nombre_habito):
        if nombre_habito not in self.habitos['Hábito'].values:
            nuevo_habito = pd.DataFrame({'Hábito': [nombre_habito], 'Completado': [False], 'Última Actualización': [None]})
            self.habitos = pd.concat([self.habitos, nuevo_habito], ignore_index=True)
            print(f"Hábito '{nombre_habito}' agregado con éxito.")
        else:
            print(f"¡Error! El hábito '{nombre_habito}' ya existe.")

    def marcar_completado(self, nombre_habito):
        if nombre_habito in self.habitos['Hábito'].values:
            index = self.habitos.index[self.habitos['Hábito'] == nombre_habito].tolist()[0]
            self.habitos.at[index, 'Completado'] = True
            self.habitos.at[index, 'Última Actualización'] = datetime.now()
            print(f"Hábito '{nombre_habito}' marcado como completado.")
        else:
            print(f"¡Error! El hábito '{nombre_habito}' no existe.")

    def borrar_habito(self, nombre_habito):
        if nombre_habito in self.habitos['Hábito'].values:
            self.habitos = self.habitos[self.habitos['Hábito'] != nombre_habito]
            print(f"Hábito '{nombre_habito}' eliminado con éxito.")
        else:
            print(f"¡Error! El hábito '{nombre_habito}' no existe.")

    def mostrar_habitos(self):
        if self.habitos.empty:
            print("No hay hábitos registrados.")
        else:
            print("Lista de hábitos:")
            print(self.habitos)

# Ejemplo de uso
usuario = "ejemplo_usuario"
manager = HabitosManager(usuario)

while True:
    print("\n=== Menú ===")
    print("1. Agregar Hábito")
    print("2. Marcar Hábito como Completado")
    print("3. Borrar Hábito")
    print("4. Mostrar Hábitos")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre_habito_nuevo = input("Ingresa el nombre del nuevo hábito: ")
        manager.agregar_habito(nombre_habito_nuevo)
    elif opcion == '2':
        nombre_habito_completado = input("Ingresa el nombre del hábito completado: ")
        manager.marcar_completado(nombre_habito_completado)
    elif opcion == '3':
        nombre_habito_borrar = input("Ingresa el nombre del hábito a borrar: ")
        manager.borrar_habito(nombre_habito_borrar)
    elif opcion == '4':
        manager.mostrar_habitos()
    elif opcion == '5':
        manager.guardar_datos()
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")