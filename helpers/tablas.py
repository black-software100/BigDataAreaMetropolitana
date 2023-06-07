def crearTablas(dataFrame,nombreTable):
    archivoHtml = dataFrame.to_html()
    archivo = open(f"./tables/{nombreTable}.html","w",encoding="utf-8")
    archivo.write(archivoHtml)
    archivo.close()