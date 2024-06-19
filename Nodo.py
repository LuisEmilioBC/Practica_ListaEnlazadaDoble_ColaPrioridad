class Nodo:
    """
    dato = numeros, objetos, palabras, etc
    """
    def __init__(self,dato):
        self.dato=dato
        self.anterior= None
        self.siguiente=None
        
    def get_dato(self):
        return self.dato
    
    def set_dato(self,dato):
        self.dato=dato
        
    def get_anterior(self):
        return self.anterior
    
    def set_anterior(self,anterior):
        self.anterior=anterior
    
    def get_siguiente(self):
        return self.siguiente
    
    def set_siguiente(self,siguiente):
        self.siguiente=siguiente
