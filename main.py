import pandas as pd
from helpers.tablas import crearTablas
from helpers.graficaBarras import graficaBarraHectarias , graficaBarraArboles
from helpers.graficaTorta import graficaPromedio
csv = pd.read_csv("./data/Siembras.csv")

# filtro 1
SanteFeDeAntiquia = csv.query("Arboles>250 and Ciudad == 'Santa Fe de Antioquia'")
crearTablas(SanteFeDeAntiquia,"tabla_santafe")

# filtro 2
Caucasia = csv.query("Ciudad == 'Caucasia'")
crearTablas(Caucasia,"tabla_Caucasia")
estadistica = Caucasia.describe().round()
crearTablas(Caucasia,"tabla_Caucasia_Descripcion")
graficaBarraHectarias(Caucasia,"Vereda","Hectareas","graficaHectariasCuacasia")
graficaBarraArboles(Caucasia,"Vereda","Arboles","graficaArbolesCuacasia")

#filtro 3

VerdaSalazar = csv.query("Vereda == 'La Salazar'")
crearTablas(VerdaSalazar,"tabla_Salazar")
VeredadRioArriba = csv.query("Vereda == 'Rio Arriba'")
crearTablas(VeredadRioArriba,"tabla_RioArriba");


# filtro 4
VeredadQuitasol = csv.query("Ciudad == 'Bello' and Vereda == 'Quitasol'")
crearTablas(VeredadQuitasol,"tabla_Bello")
graficaPromedio(VeredadQuitasol,[50,100,250,500],'Arboles','Hectareas','Promedio')

#filtro 5
Verdadcaramanta = csv.query("Ciudad == 'Caramanta' and Arboles>100")
crearTablas(Verdadcaramanta,"tabla_caramanta")

#filtro 6 
Veredadmallarino = csv.query("Vereda == 'mallarino'")
crearTablas(Veredadmallarino,"tabla_caramanta")
