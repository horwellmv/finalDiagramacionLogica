#----------- PUNTO 1 ----------------------------------------------------------------------------------------------------------------------------
# Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo
# y  permitir el ingreso de 3 notas . Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos.

def creador_lista():
    lista_alm =[]
    salida = ""

    while salida != "SI":
        nombre = (input("Ingrese nombre completo del alumno : "))
        nota1 = float(input("Ingrese nota 1: "))
        while nota1 < 0 or nota1 > 10:
            nota1 = float(input(f"Error, la nota debe ser entre 0 y 10, ingrese de nuevo nota 1: "))
        nota2 = float(input("Ingrese nota 2: "))
        while nota2 < 0 or nota2 > 10:
            nota2 = float(input(f"Error, La nota debe ser entre 0 y 10, ingrese de nuevo nota 2: "))
        nota3 = float(input("Ingrese nota 3: "))
        while nota3 < 0 or nota3 > 10:
            nota3 = float(input(f"Error, la nota debe ser entre 0 y 10, ingrese de nuevo nota 3: "))
        prom = (nota1 + nota2 + nota3) / 3

        nuevo_alumno = {"Nombre" : nombre.upper(), "Nota1" : nota1 , "Nota2" : nota2 , "Nota3" : nota3 , "Promedio" : round(prom,3) }
        lista_alm.append(nuevo_alumno)
        salida = input("""
Desea salir? escriba: si
Para agregar otro alumno presione ENTER
si / ENTER: """).upper()

    return lista_alm


lista_alumnos = creador_lista()


# ----------- PUNTO 2--------------------------------------------------------------------------------------------------------------------------------
#Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuantos desaprobaron, teniendo en cuenta que se aprueba con 4.
#La nota será el promedio de las 3 notas para cada alumno.

def clasificador (lista):
    aprobados = []
    desaprobados = []

    for alumno in lista:
        if (alumno["Promedio"] < 4):
            desaprobados.append(alumno)
        else:
            aprobados.append(alumno)
    return len(aprobados),len(desaprobados)


lista_clasificada = clasificador(lista_alumnos)

print (f"""
Cantidad de alumnos aprobados: {lista_clasificada[0]}
Cantidad de alumnos desaprobados: {lista_clasificada[1]}
""")

# ------------ PUNTO 3 ------------------------------------------------------------------------------------------------------------------------------
# Informar el promedio de nota del curso total.

def promedio_curso(lista):
    suma = 0
    contador = len(lista)

    for alumno in lista:
        suma += (alumno["Promedio"])

    return round(suma / contador,3)

resultado_curso = promedio_curso(lista_alumnos)

print (f"El promedio del curso es de: {resultado_curso}")

print("") #Solo para separar el punto del anterior y que le sea mas legible el resultado en la terminal.

# ----------- PUNTO 4 -------------------------------------------------------------------------------------------------------------------------------
# Realizar una función que indique quien tuvo el promedio más alto y quien tuvo la nota promedio más baja.


def prom_Min_Max(lista):
    estandar = 0
    min_Prom = []
    max_Prom = []

    for alumno in lista:
        if (alumno["Promedio"] == estandar):
            max_Prom.append(alumno["Nombre"])

        elif (alumno["Promedio"] > estandar):
            estandar = alumno["Promedio"]
            max_Prom = []
            max_Prom.append(alumno["Nombre"])
    for alumno in max_Prom:
        print (f"Promedio mas alto: {alumno} con {round(estandar,3)}")

    estandar = estandar - 0.001

    for alumno in lista:
        if (alumno["Promedio"] < estandar):
            estandar = alumno["Promedio"]
            min_Prom = []
            min_Prom.append(alumno["Nombre"])

        elif (alumno["Promedio"] == estandar):
            min_Prom.append(alumno["Nombre"])
    for alumno in min_Prom:
        print (f"Promedio mas bajo: {alumno} con {round(estandar,3)}")


prom_Min_Max(lista_alumnos)

print("") #Solo para separar el punto del anterior y que le sea mas legible el resultado en la terminal.

#----------- PUNTO 5 --------------------------------------------------------------------------------------------------------------------------------
# Realizar una función que permita buscar un alumno por nombre, siendo el nombre completo o parcial,
# y devuelva una lista con los n alumnos que concuerden con ese nombre junto con todos sus datos, incluido el promedio de sus notas.
# Por ejemplo :
#
# Entrada: Juan
# Salida: [
# {"nombre": "Juan Perez", "notas": [ 2, 5, 9], "promedio": 5.33},
# {"nombre": "Juana Vega", "notas": [ 5, 5, 6], "promedio": 5.33}
# ]

# Solucion alternativa mas completa. Pero no devuelve lista, hace print de los resultados.

# def buscador(lista):
#     salir = ""
#
#     while salir != "SI":
#         estudiante = input("Nombre del alumno a buscar: ")
#         resultados = 0
#         for alumno in lista:
#             if estudiante.upper() in alumno["Nombre"]:
#                 resultados += 1
#                 print(alumno)
#
#         if resultados == 0:
#             print(f"""
# No se encontraron resultados de {estudiante.upper()}.""")
#
#
#         salir = input("""
# Para una nueva busqueda oprima ENTER,
# Para salir escriba: si
# si / ENTER: """).upper()
#
#--------------------------------------------------------------------- Hé comentado el anterior porque despues de hacerlo,revisando cualquier error antes de enviarlo,
#--------------------------------------------------------------------- me di cuenta que pides que regrese una lista. por esa razón lo hice de nuevo.


def buscador(lista):

    lista_resultados = []
    estudiante = input("Nombre del alumno a buscar: ")

    for alumno in lista:
        if estudiante.upper() in alumno["Nombre"]:
            lista_resultados.append(alumno)

    return lista_resultados



lista_encontrada = buscador(lista_alumnos)

print (lista_encontrada)
