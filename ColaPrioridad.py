import heapq

class ColaPrioridad:
    def __init__(self):
        self._cola = []
        self._indice = 0

    def push(self, dato, prioridad):
        heapq.heappush(self._cola, (-prioridad, self._indice, dato))
        self._indice += 1

    def pop(self):
        if self._cola:
            return heapq.heappop(self._cola)[-1]
        else: 
            return
        
    def tamaño(self):
        return len(self._cola)
    
    def buscar(self, dato):
        indice = None
        for x in range(len(self._cola)):
            if self._cola[x][-1].get_cedula()==dato:
                indice = x+1
        return indice
    def __str__(self) -> str:
        string = ""
        for x in self._cola:
            string += x[-1].__str__()
        return string