from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Ejemplo de HTML</title>
</head>
<body>
    <div id="padre">
        <h1>Título del Padre</h1>
        <div class="hijo">
            <h2>Título del Hijo 1</h2>
            <p>Contenido del Hijo 1</p>
        </div>
        <div class="hijo">
            <h2>Título del Hijo 2</h2>
            <p>Contenido del Hijo 2</p>
        </div>
    </div>
</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")
etiqueta_padre = soup.find("div", attrs={"id": "padre"})
if etiqueta_padre:
    etiquetas_hijo = etiqueta_padre.find_all("div", attrs={"class": "hijo"})
    for etiqueta_hijo in etiquetas_hijo:
        etiqueta_titulo = etiqueta_hijo.find("h2")
        if etiqueta_titulo:
            titulo = etiqueta_titulo.text.strip()
            print(titulo)
        else:
            print("No se encontró el título del hijo")
else:
    print("No se encontró la etiqueta padre")
