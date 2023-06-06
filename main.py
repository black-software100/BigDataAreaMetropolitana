import pandas as pd
from helpers.crearTablas import crearTabla
from helpers.graficandoBarras import promediosHectarias
arboles = pd.read_csv("./data/Siembras.csv")

datos = pd.DataFrame(arboles,columns=["Ticket","Nombre comun","Fecha","evento","Ciudad","Vereda","Arboles","Hectareas"])

# filtro 1
santafeAntioquia = datos.query(' Arboles>250 and Ciudad == "Santa Fe de Antioquia"')

#filtro 2

caucasia = datos.query('Ciudad == "Caucasia"')

# print(caucasia)

crearTabla(santafeAntioquia,"tablaSantafeDeAntiqouia")


#graficas

promediosHectarias(caucasia,"Vereda","Hectareas","promCaucasia")