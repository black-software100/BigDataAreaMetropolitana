import pandas as pd
from helpers.crearTablas import crearTabla
from helpers.graficaBarras import graficaBarraHectarias , graficaBarraArboles
from helpers.graficaTorta import graficaPromedio
from os import system, chdir, getcwd
csv = pd.read_csv("./data/Siembras.csv")

# filtro 1
# SanteFeDeAntiquia = csv.query("Arboles>250 and Ciudad == 'Santa Fe de Antioquia'")
# crearTabla(SanteFeDeAntiquia,"tabla_santafe")
# graficaBarraHectarias(SanteFeDeAntiquia,"Vereda","Hectareas","graficaHectariasSantafe")
# graficaBarraArboles(SanteFeDeAntiquia,"Vereda","Arboles","graficaArbolesSantafe")

# filtro 2
# Caucasia = csv.query("Ciudad == 'Caucasia'")
# crearTabla(Caucasia,"tabla_Caucasia")
# estadistica = Caucasia.describe().round()
# crearTabla(Caucasia,"tabla_Caucasia_Descripcion")
# graficaBarraHectarias(Caucasia,"Vereda","Hectareas","graficaHectariasCuacasia")
# graficaBarraArboles(Caucasia,"Vereda","Arboles","graficaArbolesCuacasia")

#filtro 3

# VerdaSalazar = csv.query("Vereda == 'La Salazar'")
# crearTabla(VerdaSalazar,"tabla_Salazar")
# estadistica = VerdaSalazar.describe().round()
# crearTabla(estadistica,"estadisticaSalazar")
# VeredadRioArriba = csv.query("Vereda == 'Rio Arriba'")
# crearTabla(VeredadRioArriba,"tabla_RioArriba");
# estadistica = VeredadRioArriba.describe().round()
# crearTabla(estadistica,"estadisticaRioArriba");

# filtro 4
# VeredadQuitasol = csv.query("Ciudad == 'Bello' and Vereda == 'Quitasol'")
# crearTabla(VeredadQuitasol,"tabla_Quitasol")
# graficaPromedio(VeredadQuitasol,[50,100,250,500],'Arboles','Hectareas','PromedioArboles')
# graficaBarraHectarias(VeredadQuitasol,"Hectareas","Arboles","graficaArbolesQuitasol")



#filtro 5
# Verdadcaramanta = csv.query("Ciudad == 'Caramanta' and Arboles>100")
# print(Verdadcaramanta)
# crearTabla(Verdadcaramanta,"tabla_caramanta")
# graficaBarraHectarias(Verdadcaramanta,"Vereda","Hectareas","graficaHectariascaramanta")
# graficaBarraArboles(Verdadcaramanta,"Vereda","Arboles","graficaArbolescaramanta")

#filtro 6 
# Veredadmallarino = csv.query("Vereda == 'Mallarino'")
# crearTabla(Veredadmallarino,"tabla_mallarino")
# estadistica = Veredadmallarino.describe().round()
# crearTabla(estadistica,"mallarino")
# print(Veredadmallarino)

# chdir("front/")



# system("ionic serve")