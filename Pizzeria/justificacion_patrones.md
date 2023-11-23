En este primer ejercicio hemos usado dos patrones de diseño, builder y composite en dos situaciones distintas. 

La primera hemos aplicado el patrón builder para la realización de un menú pizza desde cero. Contiene los métodos abstractos de la bebida, postre y las bases de una pizza, como base, salsa, ingrediente, cocción, etc. Todo ello se añade a un objeto que lo almacena y se añadirá a un csv junto con un id y el precio asociado. 

En la segunda hemos utilizado el parón builder para realizar combos y combos personalizados, donde se guarda la bebida, el postre, el tipo de pizza que ha seleccionado, nombre del combo y el precio total. Al igual que en el anterior todos estos datos se guardan en un objeto que se subirá a un csv junto con un id. 

En ambos casos se utiliza el manejo del patrón composite para el cálculo total del precio del pedido. Este se encarga de crea una hoja para cada elemento del pedido y añadirla para componer y sumar su coste. 

Justificación de ambos patrones:
Hemos utilizado el patrón builder porque en ambos casos realizamos objetos complejos que dividimos en varias partes para tener un mayor control sobre él. 
En el caso del composite, es por su estructura de árbol y la opción de poder manejar los objetos de forma individual o grupal. 
