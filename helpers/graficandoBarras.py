import matplotlib.pyplot as plt

def promediosHectarias(dataFrame,columnax,columnay,nombregraficas):

    colores = ['green','blue','red']

    hectarias = dataFrame.groupby(columnax)[columnay].mean()
    plt.figure(figsize=(10, 8))
    plt.bar(hectarias.index,hectarias,color=colores)
    plt.xlabel("veredas")
    plt.ylabel("Hectarias")
    plt.title("promedio de hectarias")
    
    plt.savefig(f"./assets/img/{nombregraficas}.svg",dpi=100,bbox_inches="tight")