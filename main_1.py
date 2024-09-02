# Variables globales para almacenar los datos de los vehículos
n_vehiculos = 0
n_ruedas = 0
n_velocidad = 0
n_cilindrada = 0

# Función para verificar si la entrada es un número entero
def esInt():    
    try:
        global n_vehiculos
        n_vehiculos = int(input("Cuantos Vehículos desea insertar: "))
    except ValueError:
        print("ERROR! debe ingresar un número entero") 
        esInt()

# Función para solicitar el número de ruedas
def ruedas():    
    try:
        global n_ruedas
        n_ruedas = int(input("Inserte el número de ruedas: "))
    except ValueError:
        print("ERROR! debe ingresar un número entero") 
        ruedas()

# Función para solicitar la velocidad en km/h
def velocidad():    
    try:
        global n_velocidad
        n_velocidad = int(input("Inserte la velocidad en km/h: "))
    except ValueError:
        print("ERROR! debe ingresar un número entero") 
        velocidad()

# Función para solicitar el cilindraje en cc
def cilindraje():    
    try:
        global n_cilindrada
        n_cilindrada = int(input("Inserte el cilindraje en cc: "))
    except ValueError:
        print("ERROR! debe ingresar un número entero") 
        cilindraje()

# Importamos la clase Automovil desde peaje
from peaje import Automovil      

# Lista para almacenar los objetos de los vehículos
lista = []

# Solicitamos la cantidad de vehículos que se desea insertar
esInt()

# Ciclo para ingresar los datos de cada vehículo
for i in range(n_vehiculos):
    print(f"Datos del automóvil {(i+1)} :")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    ruedas()
    velocidad()
    cilindraje()
    vehic = Automovil(marca, modelo, n_ruedas, n_velocidad, n_cilindrada)
    lista.append(vehic)

# Imprimimos los datos de todos los vehículos ingresados
for i, j in enumerate(lista):
    print(f"Datos del automovil {i+1}: Marca {j.marca}, Modelo {j.modelo}, ruedas {j.n_ruedas}, {j.velocidad} Km/h, {j.cilindrada} cc")

