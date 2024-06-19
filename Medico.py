from Paciente import Paciente
from ColaPrioridad import ColaPrioridad

class Medico:
    def __init__(self, id : int, nombre : str):
        self.id = id
        self.nombre = nombre
        self.cola = ColaPrioridad()
        
    def ingresar_paciente(self, paciente : Paciente):
        self.cola.push(paciente, paciente.get_prioridad())
        
    def atender_paciente(self):
        return self.cola.pop()
    
    def numero_pacientes(self):
        return self.cola.tamaño()
    
    def buscar_paciente(self,cedula_paciente):
        return self.cola.buscar(cedula_paciente)
        
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre : str):
        self.nombre = nombre
        
    def __str__(self) -> str:
        return f"\nNOMBRE DEL MÉDICO : {self.nombre}\n\nLISTA DE PACIENTES DEL MÉDICO: \n{self.cola}\n\n     --- fin de la lista ---     "
    