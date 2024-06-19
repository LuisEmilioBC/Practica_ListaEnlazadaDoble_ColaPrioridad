#Práctica Listas Doblemente Enlazadas y colas de prioridad asignada en la clase 7
#Primer Práctica Listas Doblemente Enlazadas y Colas de Prioridad.

from Medico import Medico
from Paciente import Paciente
from ListaDoble import ListaDobleEnlazada

def intinput(string : str):
    bandera = False
    while not bandera:
        try:
            entero = int(input(string))
            bandera = True
        except ValueError:
            print('''
--------------------------------------------------
ERROR. No es un entero válido. Inténtelo de nuevo.
--------------------------------------------------
''')
    return entero         
            
def strinput(string : str):
    bandera = False
    while not bandera:
        cadena = input(string)
        if cadena != "":
            bandera = True
        else:
            print('''
----------------------------------------------------------
ERROR. No puede ingresar datos vacíos. Inténtelo de nuevo.
----------------------------------------------------------
''')
    return cadena

def prioridad():
    bandera = False
    while not bandera:
        prioridad = intinput('''Ingrese la prioridad de la emergencia:
1. VERDE
2. AMARILLO
3. ROJO
Prioridad : ''')
        if prioridad not in (1,2,3):
            print('''
-----------------------------------------
ERROR. La prioridad debe ser de 1, 2 ó 3.
-----------------------------------------
''')
        else:
            bandera = True
    return prioridad

lista = ListaDobleEnlazada()
opcion = 0

while opcion != 9:
    opcion = intinput("""
Ingrese la opción que requiera:
    1. Registrar médico
    2. Registrar paciente
    3. Consultar médico
    4. Mostrar el siguiente paciente en atender
    5. Consultar paciente
    6. Mostrar la lista de médicos del primero al último
    7. Mostrar la lista de médicos del último al primero
    8. Calcular el total de pacientes por atender
    9. Salir
Opción : """)
    match opcion:
        case 1:
            lista.agregar_medico_final(Medico(intinput('\nIngrese el ID del médico : '),strinput('Ingrese el nombre del médico : ')))
        case 2:
            lista.agregar_paciente(Paciente(intinput('\nIngrese la cédula del paciente : '),strinput('Ingrese el nombre del paciente : '),intinput('Ingrese la edad del paciente : '),prioridad()))
        case 3:
            if (medico := lista.consultar_medico(intinput('\nIngrese el ID del médico : '))):
                print(medico)
            else:
                print('''
-----------------------------------------
ATENCIÓN: No existe un médico con ese ID.
-----------------------------------------
''')
        case 4:
            if (paciente := lista.atender_paciente(intinput('\nIngrese el ID del médico disponible : '))):
                print(paciente)
            else:
                print('''
-------------------------------------------
ATENCIÓN: El médico no tiene más pacientes.
-------------------------------------------
''')
        case 5:
            if (tupla := lista.consultar_paciente(intinput('\nIngrese la cédula del paciente : '))):
                print(f'\nEl paciente está registrado en la posición {tupla[0]}, de la fila del médico: {tupla[1].get_nombre()}, ID: {tupla[1].get_id()}')
            else:
                print('''
-------------------------------------------------
ATENCIÓN: El paciente no se encuentra registrado.
-------------------------------------------------
''')
        case 6:
            lista.mostrar()
        case 7:
            lista.mostrar_inverso()
        case 8:
            print(f'\nTOTAL DE PACIENTES POR ATENDER : {lista.total_pacientes()}')
        case 9:
            print('\nSaliendo del sistema...')
        case _:
            print('''
------------------------
ERROR: Opción no válida.
------------------------
''')
