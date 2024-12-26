lista_str = ["tarea_list 1", "tarea_list 2", "tarea_list 3","tarea_list 4", "tarea_list 5" ]

tupla = ("tarea_tup 1", "tarea_tup 2", "tarea_tup 3", "tarea_tup 4", "tarea_tup 5")

diccionario = {
    "tarea_dic 1": "To Do",
    "tarea_dic 2": "WIP",
    "tarea_dic 3": "Done",
    "tarea_dic 4": "WIP",
    "tarea_dic 5": "Done"
}



#Indexing --> sirve para traer un unico valor
print("\n************** indexing **************\n")

print(f"\nAccedo al derecho de la lista: {lista_str[2]}")
print(f"accedo al reves de la lista: {lista_str[-1]}\n")


print(f"accedo a un casillero especifico de la lista: {lista_str[-2][6]}")

print(f"\nAccedo al derecho de la tupla: {lista_str[2]}")
print(f"accedo al reves de la tupla: {tupla[-1]}\n")


print("Accedo al dicionario ", diccionario["tarea_dic 3"])


#Slicing --> sirve para traer un conjunto de valores
print("\n************** Slicing **************\n")

print (f"en este caso voy a imprimir 2 valores de la lista: {lista_str[1:3]}")
print (f"en este caso voy a imprimir 2 valores de la tupla: {tupla[1:3]}")
print("\n\na los diccionarios no se puede aplicar el concepto de Slicing\n")


#stride --> permite poner una 3era condicion para traer datos
print("\n************** Stride **************\n")

print (f"imprimo desde la poscion 2 de la lista y especifico que lo haga de 2 en 2 {lista_str[2::2]}")
print (f"imprimo desde la poscion 1 de la lista y especifico que lo haga cada 3 {lista_str[1::3]}")
print (f"imprimo desde la poscion 1 de la tupla y especifico que lo haga cada 3 {tupla[1::3]}")

print("\n\ncon los diccionarios no se puede hacer el Stride\n")


#Modificacion
print("\n************** Modificar / editar **************\n")

lista_str[2] = "tarea_modificada"
print(f"modifique la 'tarea_list 3' por: {lista_str}")

diccionario["tarea_dic 2"] = "work in progress"
print(f"modifique la 'tarea_dic 2' por: {diccionario}")
