Justificación del uso del patrón Builder

El patrón Builder nos permite crear objetos complejos paso a paso, en otras palabras, 
dividir el objeto en múltiples partes para tener un mayor control y flexibilidad sobre él. 
Además, nos permite crear diferentes tipos de objetos utilizando el mismo proceso de construcción.
Lo cual, es bastante útil cuando queremos crear objetos que sigan una misma estructura, pero que tengan diferentes partes o contenido. 

Es el caso de la pizzería, donde tenemos una estructura básica de una pizza, pero 
cada una es única, debido a la gran variedad de ingredientes que existen.

Descartamos el resto de patrones:
- El patrón Abstract Factory (crear familias de objetos relacionados) 
implicando que en este ejercicio un Abstract sería las pizzas, otro las bebidas, etc., pero en nuestro ejercicio lo queremos todo junto como un único pedido. 

- El patrón Factory Method, es para cuando queremos crear objetos no muy complicados. 
Este patrón sería útil si tuviésemos tipos de pizzas más genéricos. 

- El patrón Prototype, sirve para crear objetos copiando uno ya existente. Sería útil en el caso de querer crear pizzas con alguna pequeña variación, pero aquí queremos generarla desde cero a gusto del consumidor. 

- El patrón Singleton, es para cuando queremos que solo exista una instancia de un objeto. Lo cual, no sirve para crear las pizzas. Sería mejor para administrar recursos compartidos, como por ejemplo, el horno de la pizzería.

