import matplotlib.pyplot as plt

def graficaBarraHectarias(dataFrame,columnax,columnay,nombregrafica):

    colores = ['#7FB3D5', '#45B39D', '#F4D03F', '#F5B041','#EC7063']

    hectariasPromedio = dataFrame.groupby(columnax)[columnay].mean()
    plt.figure(figsize=(10, 8))
    plt.bar(hectariasPromedio.index,hectariasPromedio,color=colores)
    plt.xlabel("Veredas")
    plt.ylabel("Hectarias promedio")
    plt.title("Hectarias promedio por veredas")
    plt.savefig(f"./front/src/assets/img/{nombregrafica}.svg",dpi=300,bbox_inches="tight")


def graficaBarraArboles(dataFrame,columnax,columnay,nombregrafica):

    colores = ['#7FB3D5', '#45B39D', '#F4D03F', '#F5B041','#EC7063']

    hectariasPromedio = dataFrame.groupby(columnax)[columnay].mean()
    plt.figure(figsize=(10, 8))
    plt.bar(hectariasPromedio.index,hectariasPromedio,color=colores)
    plt.xlabel("Veredas")
    plt.ylabel("Arboles promedio")
    plt.title("Arboles promedio por veredas")
    plt.savefig(f"./front/src/assets/img/{nombregrafica}.svg",dpi=300,bbox_inches="tight")


