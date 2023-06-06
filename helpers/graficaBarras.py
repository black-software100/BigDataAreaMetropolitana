import matplotlib.pyplot as plt

def graficaBarraHectarias(dataFrame,columnax,columnay,nombregrafica):

    colores = ['#7FB3D5', '#45B39D', '#F4D03F', '#F5B041','#EC7063']

    hectariasPromedio = dataFrame.groupby(columnax)[columnay].mean()
    plt.figure(figsize=(10, 8))
    plt.bar(hectariasPromedio.index,hectariasPromedio,color=colores)
    plt.xlabel("Veredas")
    plt.ylabel("Hectarias promedio")
    plt.title("Hectarias promedio por veredas")
    plt.savefig(f"./assets/img/{nombregrafica}.svg",dpi=300,bbox_inches="tight")


def graficaBarraArboles(dataFrame,columnax,columnay,nombregrafica):

    colores = ['#7FB3D5', '#45B39D', '#F4D03F', '#F5B041','#EC7063']

    hectariasPromedio = dataFrame.groupby(columnax)[columnay].mean()
    plt.figure(figsize=(10, 8))
    plt.bar(hectariasPromedio.index,hectariasPromedio,color=colores)
    plt.xlabel("Veredas")
    plt.ylabel("Arboles promedio")
    plt.title("Arboles promedio por veredas")
    plt.savefig(f"./assets/img/{nombregrafica}.svg",dpi=300,bbox_inches="tight")


# #Crear instancia de la clase FPDF
# pdf = FPDF()
# # Agregar página
# pdf.add_page()
# # Establecer fuente y tamaño de letra
# pdf.set_font("Arial", size=12)
# # Establecer color de línea
# pdf.set_draw_color(0, 0, 0)  # Color negro
# # Dibujar título de la tabla
# pdf.cell(200, 10, txt="Tabla de analistas1:", ln=1, align="L")
# # Obtener los datos de la tabla analistas1
# tabla_analistas1 = analistas1.to_string()
# # Dividir los datos en filas
# filas = tabla_analistas1.split("\n")
# # Dibujar filas y column