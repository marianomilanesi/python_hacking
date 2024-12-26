"""""""""
Práctica Listas, Tuplas y Diccionarios
Objetivo:
Este ejercicio está diseñado para consolidar tu comprensión de las listas, tuplas, diccionarios, y los conceptos de indexing, slicing y stride en Python. Al finalizar, habrás creado un menú de un restaurante ficticio, utilizando estas estructuras de datos de manera creativa y efectiva.

Instrucciones:
Creación del Menú:
Crea una lista llamada platos que contenga los siguientes platos (strings): Paella, Risotto, Sushi, Tacos y Pizza.
Crea una tupla llamada precios con los precios correspondientes a cada plato de la lista platos. Asegúrate de que el orden de los precios coincida con el de los platos. Los precios son los siguientes:
Paella: 15 $
Risotto: 12 $
Sushi: 20 $
Tacos: 10 $
Pizza: 8 $
Utiliza slicing para crear una lista platos_seleccionados que contenga los nombres del segundo al cuarto plato de la lista platos.
Crea un diccionario menu donde cada clave sea un nombre de plato y su valor correspondiente sea el precio.

Exploración del Menú:
Imprime el menú completo por pantalla.
Utiliza indexing para imprimir el nombre y el precio del tercer plato del menú.
Utiliza stride en la lista platos para crear una nueva lista platos_pares que contenga solo los platos en posiciones pares e imprímelos.

Resultado Esperado:
Bienvenidos a nuestro menú especial:
- Paella:15 $
- Risotto: 12 $
- Sushi: 20 $
- Tacos: 10 $
- Pizza: 8 $
El tercer plato es Sushi y su precio es 20.
Los platos pares son: ['Paella', 'Sushi', 'Pizza']

Notas para el Estudiante:
Recuerda que el indexing en Python comienza en 0.
Para aprobar esta evaluación tu respuesta debe coincidir exactamente con los datos presentados en la sección "Resultado esperado".
Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio. En esta pestaña puedes ver el código de solución de esta práctica.
"""""""""

platos = ["Paella", "Risotto", "Sushi", "Tacos", "Pizza"]
precios = (15, 12, 20, 10, 8)

platos_seleccionados = platos[1:4]
menu = {
    platos[0]: precios[0],    
    platos[1]: precios[1],
    platos[2]: precios[2],
    platos[3]: precios[3],
    platos[4]: precios[4]
}

tercer_plato = platos[2]
precio_tercer_plato = menu[tercer_plato]


print("\nBienvenido al Restaurante\n")
print(f"\n - Paella: ${menu['Paella']}")
print(f"\n - Risotto: ${menu['Risotto']} ")
print(f"\n - Sushi: ${menu['Sushi']}")
print(f"\n - Tacos: ${menu['Tacos']}")
print(f"\n - Pizza: ${menu['Pizza']}")
print(f"El tercer plato es: {tercer_plato} y su precio es ${precio_tercer_plato}")
print(f"los plato pares son: {platos_seleccionados}")



#***********************************