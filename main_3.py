# Importamos las clases necesarias desde peaje
from peaje import Automovil, Particular, Carga, Bicicleta, Motocicleta, Vehiculo

# Creamos instancias de cada tipo de vehículo
particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Guardamos los datos en un vehic CSV
particular.guardar_datos_csv("vehic.csv", particular)
carga.guardar_datos_csv("vehic.csv", carga)
bicicleta.guardar_datos_csv("vehic.csv", bicicleta)
motocicleta.guardar_datos_csv("vehic.csv", motocicleta)

# Leemos y mostramos los datos del vehic CSV
from peaje import Leervehic
v = Leervehic("vehic.csv")
v.leer_datos_csv()





