import datetime
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class NodoMantenimiento:
    def __init__(self, mantenimiento):
        self.mantenimiento = mantenimiento
        self.siguiente = None

class ListaMantenimiento:
    def __init__(self):
        self.cabeza = None  
    
    def AgregarMantenimiento(self, mantenimiento):
        nuevoNodo = NodoMantenimiento(mantenimiento)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo

    def MostrarMantenimiento(self):
        actual = self.cabeza
        if actual is None:
            print("No hay mantenimientos registrados.")
        while actual:
            print(actual.mantenimiento)
            actual = actual.siguiente

    def CalcularCosto(self):
        total = 0
        actual = self.cabeza
        while actual:
            total += actual.mantenimiento.costo
            actual = actual.siguiente
        return total

class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha if self.ValidarFecha(fecha) else "Fecha inválida"
        self.descripcion = descripcion
        self.costo = costo if self.ValidarCosto(costo) else 0

    def ValidarFecha(self, fecha):
        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def ValidarCosto(self, costo):
        return costo > 0
    
    def __str__(self):    
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}, Costo: {self.costo}"

class NodoVehiculo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.siguiente = None

class FlotaVehiculos:
    def __init__(self):
        self.cabeza = None
    
    def AgregarVehiculo(self, vehiculo):
        nuevoNodo = NodoVehiculo(vehiculo)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo

    def EliminarVehiculo(self, placa):
        actual = self.cabeza
        anterior = None
        while actual and actual.vehiculo.placa != placa:
            anterior = actual
            actual = actual.siguiente
        
        if actual:
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            del actual
            print("Vehículo eliminado exitosamente.")
        else:
            print("No se encontró un vehículo con esa placa.")

    def BuscarVehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.vehiculo.placa == placa:
                print(actual.vehiculo)
                return actual.vehiculo
            actual = actual.siguiente
        print("Vehículo no encontrado.")
        return None

    def ListarVehiculos(self):
        actual = self.cabeza
        if actual is None:
            print("No hay vehículos registrados.")
        while actual:
            print(actual.vehiculo)
            actual = actual.siguiente

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.placa = placa if self.validar_placa(placa) else "Placa inválida"
        self.marca = marca
        self.modelo = modelo
        self.año = año if self.validar_año(año) else "Año inválido"
        self.kilometraje = kilometraje if self.validar_kilometraje(kilometraje) else 0
        self.historial = ListaMantenimiento()
    
    def validar_placa(self, placa):
        return len(placa) == 7 and placa[:3].isalpha() and placa[3:].isdigit()
    
    def validar_año(self, año):
        return 1900 < año <= datetime.datetime.now().year
    
    def validar_kilometraje(self, kilometraje):
        return kilometraje >= 0
    
    def __str__(self):
        return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}"


class main():
    flota = FlotaVehiculos()

    while True:
        limpiar_pantalla()
        print("MENÚ DE FLOTA DE VEHÍCULOS")
        print("1. REGISTRAR UN NUEVO VEHÍCULO")
        print("2. ELIMINAR UN VEHÍCULO POR SU PLACA")
        print("3. BUSCAR UN VEHÍCULO POR SU PLACA Y MOSTRAR INFORMACIÓN")
        print("4. LISTAR TODOS LOS VEHÍCULOS REGISTRADOS")
        print("5. AGREGAR UN MANTENIMIENTO A UN VEHÍCULO")
        print("6. CONSULTAR EL HISTORIAL DE MANTENIMIENTOS")
        print("7. CACULAR EL TOTAL DE LOS MANTENIMIENTOS")
        print("8. SALIR")
        

        print("INGRESE EL NÚMERO QUE CORRESPONDE A LA OPCIÓN QUE DESEA REALIZAR")
        op = int(input())


        if op == 1:
            limpiar_pantalla()
            print("Ingrese la placa del auto (3 letras y 4 números (ABC1234))")
            placa = input().upper()
            print("Ingrese la marca del auto")
            marca = input()
            print("Ingrese el modelo del auto")
            modelo = input()
            print("Ingrese el año del auto")
            año = int(input())
            print("Ingrese el kilometraje del auto")
            kilometraje = int(input())

            vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
            flota.AgregarVehiculo(vehiculo)

            print("Vehículo agregado con éxito.")
            input("Presione enter para continuar...")

        elif op == 2:
            limpiar_pantalla()
            print("Ingrese el número de placa del vehículo que desea eliminar")
            placa = input().upper()
            flota.EliminarVehiculo(placa)
            input("Presione enter para continuar...")

        elif op == 3:
            limpiar_pantalla()
            print("Ingrese el número de placa del vehículo que desea buscar")
            placa = input().upper()
            flota.BuscarVehiculo(placa)
            input("Presione enter para continuar...")

        elif op == 4:
            limpiar_pantalla()
            print("LISTA DE VEHÍCULOS REGISTRADOS:")
            flota.ListarVehiculos()
            input("Presione enter para continuar...")

        elif op == 5:
            limpiar_pantalla()
            print("Ingrese la placa del vehículo para agregar mantenimiento:")
            placa = input().upper()
            vehiculo = flota.BuscarVehiculo(placa)
            if vehiculo:
                print("Ingrese la fecha del mantenimiento (año-mes-dìa):")
                fecha = input()
                print("Ingrese la descripción del mantenimiento:")
                descripcion = input()
                print("Ingrese el costo del mantenimiento:")
                costo = float(input())
                mantenimiento = Mantenimiento(fecha, descripcion, costo)
                vehiculo.historial.AgregarMantenimiento(mantenimiento)
                print("Mantenimiento agregado exitosamente.")
            else:
                print("Vehículo no encontrado.")
            input("Presione enter para continuar...")

        elif op == 6:
            limpiar_pantalla()
            print("Ingrese la placa del vehículo para ver el historial de mantenimientos:")
            placa = input().upper()
            vehiculo = flota.BuscarVehiculo(placa)
            if vehiculo:
                vehiculo.historial.MostrarMantenimiento()
            else:
                print("Vehículo no encontrado.")
            input("Presione enter para continuar...")

        elif op == 7:
            limpiar_pantalla()
            print("Ingrese la placa del vehículo para calcular el total de mantenimientos:")
            placa = input().upper()
            vehiculo = flota.BuscarVehiculo(placa)
            if vehiculo:
                print("Total de costos: Q", vehiculo.historial.CalcularCosto())
            else:
                print("Vehículo no encontrado.")
            input("Presione enter para continuar...")
        elif op == 8:
            print("Saliendo del programa....")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione enter para continuar...")
              



    