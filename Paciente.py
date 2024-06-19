class Paciente:
    def __init__(self, cedula : int, nombre : str, edad : int, prioridad : int):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.prioridad = prioridad
    
    def get_cedula(self):
        return self.cedula
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre : str):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad : int):
        self.edad = edad
        
    def get_prioridad(self):
        return self.prioridad
    
    def set_prioridad(self, prioridad : int):
        self.prioridad = prioridad
        
    def __str__(self) -> str:
        return f"\nDATOS DEL PACIENTE:\nCÉDULA: {self.cedula}\nNOMBRE : {self.nombre}\nEDAD : {self.edad}\nNIVEL DE EMERGENCIA : {self.prioridad}\n"