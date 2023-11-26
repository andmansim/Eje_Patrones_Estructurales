import proxy
import composite

#creamos los documentos
doc1 = composite.Leaf("Documento 1", 'texto', 120, False)
doc2 = composite.Leaf("Documento 2", 'texto', 200, True)
doc3 = composite.Leaf("Documento 3", 'imagen', 30, False)
doc4 = composite.Leaf("Documento 4", 'video', 100, True)

#creamos las carpetas
carpeta_principal = composite.CompositeCarpeta("Carpeta Principal")
carpeta1 = composite.CompositeCarpeta("Carpeta 1")
carpeta2 = composite.CompositeCarpeta('Carpeta 2')

#creamos los enlaces
enlace1 = composite.CompositeEnlace('enlace doc1', 'Carpeta1-->Documento1')
enlace2 = composite.CompositeEnlace('enlace doc4','Carpeta2-->Documento4')

#agregamos los documentos, carpetas y enlaces a la carpeta principal
carpeta_principal.add(carpeta1)
carpeta_principal.add(carpeta2)
carpeta_principal.add(enlace1)

carpeta1.add(doc1)
carpeta1.add(doc3)
carpeta1.add(enlace2)

carpeta2.add(doc2)
carpeta2.add(doc4)

#creamos el proxy
realsub = proxy.RealSubject(carpeta_principal)
proxi = proxy.Proxy(realsub)

#pedimos datos de acceso
tipo_acceder = input('Ingrese el tipo del dato (documento, enlace, carpeta) que desea acceder:  (si desea salir escriba salir)')
doc_acceder = input('Ingrese el nombre del dato al que desea acceder: ')

while tipo_acceder != 'salir':
    #accedemos al dato
    proxy.client_code(proxi, tipo_acceder, doc_acceder)
    print('Registros de acceso: ')
print(proxi._entrada_log)