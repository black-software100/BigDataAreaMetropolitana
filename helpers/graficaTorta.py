import matplotlib.pyplot as plt
import pandas as pd

def graficaPromedio(dataFrame,rangos,columnaInteresRango,columnaApromediar,nombregrafica):
 
    figure= plt.figure()

    dataFrame['rangoNuevo'] = pd.cut(dataFrame[columnaInteresRango],bins=rangos)
  
    print (dataFrame['rangoNuevo'])
    Rango = dataFrame.groupby('rangoNuevo')[columnaApromediar].sum()
  
    valor = Rango.values
    cabecera = Rango.index

    plt.pie(valor,labels=cabecera,autopct='%1.1f%%')
    plt.title("Distribution de datos")
    plt.savefig(f"./assets/img/{nombregrafica}.svg",dpi=300,bbox_inches="tight")