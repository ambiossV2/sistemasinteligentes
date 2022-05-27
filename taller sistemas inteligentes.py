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