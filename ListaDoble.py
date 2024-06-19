from Medico import Medico
from Paciente import Paciente
from Nodo import Nodo 

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
    
    def agregar_medico_final(self, dato : Medico):
        if not self.consultar_medico(dato.get_id()):
            nuevo_nodo = Nodo(dato)
            if self.cabeza is None:
                self.cabeza = nuevo_nodo
                self.ultimo = nuevo_nodo
            else: 
                self.ultimo.set_siguiente(nuevo_nodo)
                nuevo_nodo.set_anterior(self.ultimo)
                self.ultimo = nuevo_nodo
        else:
            print('''
-----------------------------------------------------
NO SE PUDO REALIZAR: Ya existe un médico con ese ID.
-----------------------------------------------------
''')
    
    def agregar_medico_inicio(self, dato : Medico):
        if not self.consultar_medico(dato.get_id()):
            nuevo_nodo = Nodo(dato)
            if self.cabeza is None:
                self.cabeza = nuevo_nodo
                self.ultimo = nuevo_nodo
            else: 
                nuevo_nodo.set_siguiente(self.cabeza)
                self.cabeza.set_anterior(nuevo_nodo)
                self.cabeza = nuevo_nodo
        else:
            print('''
-----------------------------------------------------
NO SE PUDO REALIZAR: Ya existe un médico con ese ID.
-----------------------------------------------------
''')
            
    def agregar_paciente(self, paciente : Paciente):
        if not self.consultar_paciente(paciente.get_cedula()):
            if self.cabeza is not None:
                medico = self.cabeza.get_dato()
                actual = self.cabeza
                while actual:
                    if medico.numero_pacientes()>actual.get_dato().numero_pacientes():
                        medico=actual.get_dato()
                    actual = actual.get_siguiente()
                medico.ingresar_paciente(paciente)
            else:
                print('''
----------------------------------------------------
NO SE PUDO REALIZAR: No existen médicos registrados.
----------------------------------------------------
''')
        else:
            print('''
----------------------------------------------------------------------
NO SE PUDO REALIZAR: Este paciente ya está registrado con otro médico.
----------------------------------------------------------------------
''')
        
    def mostrar(self):
        actual = self.cabeza
        print('\nLISTA DE MÉDICOS REGISTRADOS: ')
        while actual:
            print(f"ID : {actual.dato.get_id()},    NOMBRE : {actual.dato.get_nombre()},    NÚMERO DE PACIENTES : {actual.dato.numero_pacientes()}", end='\n')
            actual = actual.get_siguiente()
        print('     ---fin de la lista---     ')
        
    def mostrar_inverso(self):
        actual = self.ultimo
        print('\nLISTA DE MÉDiCOS REGISTRADOS: ')
        while actual:
            print(f"ID : {actual.dato.get_id()},    NOMBRE : {actual.dato.get_nombre()},    NÚMERO DE PACIENTES : {actual.dato.numero_pacientes()}", end='\n')
            actual = actual.get_anterior()
        print('     ---fin de la lista---     ')
        
    def consultar_medico(self, id_medico : int):
        actual = self.cabeza
        while actual:
            if actual.get_dato().get_id() == id_medico:
                return actual.get_dato()
            actual = actual.get_siguiente()
        return
    
    def atender_paciente(self, id_medico : int):
        if (medico := self.consultar_medico(id_medico)):
            return medico.atender_paciente()
        else:
            return '''
-----------------------------------------------------
NO SE PUDO REALIZAR: No existen un médico con ese ID.
-----------------------------------------------------
'''
    
    def consultar_paciente(self, cedula_paciente : int):
        actual = self.cabeza
        while actual:
            if (indice_paciente := actual.get_dato().buscar_paciente(cedula_paciente)):
                return (indice_paciente, actual.get_dato())
            actual = actual.get_siguiente()
        return
        
    def total_pacientes(self,nodo=0):
        if nodo == 0:
            nodo = self.cabeza 
        if nodo:
            return nodo.get_dato().numero_pacientes() + self.total_pacientes(nodo.get_siguiente())
        else:
            return 0
            