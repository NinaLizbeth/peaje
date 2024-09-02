import csv

# Clase Vehiculo, base para todos los tipos de vehículos
class Vehiculo:
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    # Método para guardar los datos de un vehículo en un archivo CSV
def guardar_datos_csv(self, nombre_archivo, vehiculo):
    try:
        with open(nombre_archivo, "a", newline='') as archivo:  # Abre el archivo en modo "append"
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerow([vehiculo.__class__.__name__, vehiculo.marca, vehiculo.modelo, vehiculo.n_ruedas, *list(vehiculo.__dict__.values())[3:]])
            print(f"Datos del {vehiculo.__class__.__name__} guardados en {nombre_archivo}.")
    except FileNotFoundError:
        print(f'Error: El archivo {nombre_archivo} no se encuentra.')
    except Exception as error:
        print(f'Se ha generado un error no previsto: {type(error).__name__}')


# Clase para leer y mostrar los datos guardados en el archivo CSV
class LeerArchivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_datos_csv(self):
        try:
            with open(self.nombre_archivo, "r") as archivo:  # Abre el archivo en modo "lectura"
                archivo_csv = csv.reader(archivo)
                for fila in archivo_csv:
                    clase = fila[0]  # Primer elemento es el nombre de la clase
                    print(f"Lista de Vehículos {clase}")
                    print(", ".join(fila[1:]))  # Imprime los atributos del vehículo
        except FileNotFoundError:
            print(f"Error: El archivo '{self.nombre_archivo}' no existe.")
        except ValueError:
            print(f"Error: El archivo '{self.nombre_archivo}' no tiene un formato válido.")

    def __repr__(self):
        return str(self.__dict__)

# Clase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __repr__(self):
        return str(self.__dict__)

# Clase Particular que hereda de Automovil
class Particular(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_asiento):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_asiento = n_asiento

# Clase Carga que hereda de Automovil
class Carga(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo = tipo

# Clase Motocicleta que hereda de Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, n_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, n_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios
