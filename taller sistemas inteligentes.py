class Node:
    def __init__(self, data, level, fval):
        # Inicialice el nodo con los datos, el nivel del nodo y el valor calculado
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        # Genera nodos secundarios a partir del nodo dado moviendo el espacio en blanco ya sea en las cuatro direcciones {arriba,abajo,izquierda,derecha}
        x, y = self.find(self.data, '_')
        # val_list contiene valores de posición para mover el espacio en blanco en cualquiera de las 4 direcciones [arriba, abajo, izquierda, derecha] respectivamente.
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children
    
    def shuffle(self, puz, x1, y1, x2, y2):
        # Mueva el espacio en blanco en la dirección dada y si el valor de la posición está fuera de los límites, devuelve ninguno
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        # función de copia para crear una matriz similar del nodo dado (hijo)
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        #Usado específicamente para encontrar la posición del espacio en blanco
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j

class Puzzle:
    def __init__(self, size):
        #Inicialice el tamaño del rompecabezas por el tamaño especificado, abra y cierre las listas para vaciar
        self.n = size
        self.open = []
        self.closed = []


    def f(self, start, goal):
        return self.h(start.data, goal)

    def h(self, start, goal):
        # Calcula la diferencia entre los puzzles dados
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp