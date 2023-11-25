import proxy
import composite


doc1 = composite.Leaf("Documento 1", 'texto', 120, False)
doc2 = composite.Leaf("Documento 2", 'texto', 200, True)
doc3 = composite.Leaf("Documento 3", 'imagen', 30, False)
doc4 = composite.Leaf("Documento 4", 'video', 100, True)

carpeta_principal = composite.CompositeCarpeta("Carpeta Principal")
carpeta1 = composite.CompositeCarpeta("Carpeta 1")
carpeta2 = composite.CompositeCarpeta('Carpeta 2')

carpeta_principal.add(carpeta1)
carpeta_principal.add(carpeta2)
