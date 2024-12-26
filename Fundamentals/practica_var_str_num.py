"""""""""
Práctica Variables, Strings y Números
Objetivo:

Complementar el "Diario de un Astronauta" agregando una cabecera. Aprender a manejar variables en Python, utilizando tipos de datos básicos como números y cadenas de texto (strings).

Instrucciones:

Crea una variable llamada nombre_astronauta y asígnale tu nombre como un string.

Crea una variable edad_astronautanauta y asígnale tu edad como un número.

Crea una variable destino y asígnale el nombre de un destino como string (por ejemplo, "Marte").

Imprime un mensaje de introducción utilizando estas variables, que diga: "Hola, soy [nombre_astronauta], tengo [edad_astronautanauta] años y mi próximo destino es [destino]."

Crea dos variables, combustible y velocidad, asignándoles valores numéricos.

Imprime un mensaje que diga: "Estoy navegando a [velocidad] km/s con [combustible]% de combustible restante hacia [destino]."
*************************************************************************************************************************

Resultado esperado:

Diario de un Astronauta



Hola, soy Max, tengo 25 años y mi próximo destino es Marte.

Estoy navegando a 27000 km/s con 85% de combustible restante hacia Marte.

Fecha: 2024-01-10

Hoy experimentamos con el cultivo de plantas en microgravedad.

Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!

Fecha: 2024-01-11

Realizamos una caminata espacial para reparar un panel solar.

Mensaje personal: Flotar en el espacio nunca deja de asombrarme.

*************************************************************************************************************************
Notas para el Estudiante:

Utiliza f-strings para insertar las variables en las cadenas de texto y mostrarlas por pantalla utilizando print.

Recuerda que al usar f-strings, debes colocar el valor entre {} dentro del string. Por ejemplo: f"Texto {variable}".

Para aprobar esta evaluación tu respuesta debe coincidir exactamente con los datos presentados en la sección "Resultado esperado".

Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio. En esta pestaña puedes ver el código de solución de esta práctica.
*************************************************************************************************************************
"""""""""

nombre_astronauta = "Mariano"
edad_astronauta = 28
destino = "Marte"

combustible = 85
velocidad = 2700


print("Diario de un Astronauta \n")
print(f"Hola soy {nombre_astronauta}, tengo {edad_astronauta} y mi proximo destino es {destino}\n")
print(f"estoy navegando a {velocidad}km/s con {combustible}% de combustible restante hacia {destino}\n")
print("Fecha: 2024-01-10\n", "Hoy experimentamos con el cultivo de plantas en microgravedad.\n", "Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!", end="\n")
print ("\n")
print("Fecha: 2024-01-11\n", "Realizamos una caminata espacial para reparar un panel solar.\n", "Mensaje personal: Flotar en el espacio nunca deja de asombrarme.", end="\n")
