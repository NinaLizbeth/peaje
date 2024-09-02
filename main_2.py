# inportacion
from peaje import Automovil, Particular, Carga, Bicicleta, Motocicleta, Vehiculo

#  instancias de cada tipo de vehículo
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
print(f"Marca {particular.marca}, Modelo {particular.modelo}, {particular.n_ruedas} ruedas, {particular.velocidad} Km/h, {particular.cilindrada} cc, Puestos: {particular.n_asiento}")

carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.n_ruedas} ruedas, {carga.velocidad} Km/h, {carga.cilindrada} cc, Carga {carga.peso_carga} Kg")

bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.n_ruedas} ruedas, Tipo: {bicicleta.tipo}")

motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.n_ruedas} ruedas, Tipo: {motocicleta.tipo}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")

#verifico  instancias con isinstance
print(f"Motocicleta es instancia con relación a Vehículo:     {isinstance(motocicleta, Vehiculo)}")

print(f"Motocicleta es instancia con relación a Automovil:    {isinstance(motocicleta, Automovil)}")

print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga:   {isinstance(motocicleta, Carga)}")

print(f"Motocicleta es instancia con relación a Bicicleta:      {isinstance(motocicleta, Bicicleta)}")

print(f"Motocicleta es instancia con relación a Motocicleta:   {isinstance(motocicleta, Motocicleta)}")
