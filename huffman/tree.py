"""
Implementación de árboles binarios adaptada para usarse para el algoritmo de Huffman
Yael Chavoya
"""
from typing import List, Dict


class Node:
    """
    Representa un nodo en el árbol
    """

    def __init__(self, char: str or None = None, count: int = 0):
        """
        Inicializa las propiedades

        :param char: El carácter que representa el nodo, None si es solamente una conexión
        :param count: La frecuencia con la que aparece el carácter en el texto, una suma de la frecuencia de sus hijos
        en caso de un nodo de conexión
        """
        self.char: str or None = char
        self.count: int = count
        self.children: List[Node] = []


class Tree:
    """
    Representa el árbol del cual se formarán los códigos de los caracteres
    """

    def __init__(self, freq_dict:  Dict[str, int] or None = None):
        """
        Genera un árbol a partir de un diccionario de frecuencias de caracteres, iniciando de abajo hacia arriba.

        :param freq_dict: El diccionario de frecuencias
        """
        self.root = None

        if not freq_dict:
            return

        # Convertir el diccionario a una lista ordenada por frecuencia, de menor a mayor
        sortedlist = sorted(freq_dict.items(), key=lambda x: x[1])

        # Crear un nodo para cada elemento del diccionario
        tree_list: List[Node] = []
        for item in sortedlist:
            tree_list.append(Node(item[0], item[1]))

        # Si solo hay un carácter en el diccionario, esa es la raíz
        if len(tree_list) == 1:
            self.root = tree_list.pop(0)

        # Mientras falten nodos por agregar al árbol
        while tree_list:
            # Obtener los primeros dos items de la lista (los de menor frecuencia)
            item1 = tree_list.pop(0)
            item2 = tree_list.pop(0)

            # Crear un nodo de conexión con la suma de las frecuencias de los items, y colocar los items como hijos
            combined = Node(count=item1.count + item2.count)
            combined.children = [item1, item2]

            if not tree_list:
                # Si esos eran los últimos items, asignar el nodo de conexión como raíz
                self.root = combined
            else:
                # Si aún quedan items, agregar el nodo de conexión a la lista y ordenarla por frecuencias
                tree_list.append(combined)
                tree_list.sort(key=lambda x: x.count)
    
    def __str__(self) -> str:
        """
        Representar el árbol como una cadena de texto, uso para depuración

        :return: Una cadena con representación en texto del árbol
        """
        string = ''
        for item in self.order_bfs():
            num_children = len(item.children)
            if num_children > 0:
                string += f'Nodo {item.char} ({item.count}) children {num_children}\n'
                for child in item.children:
                    string += f'-- child: {child.char} ({child.count})\n'
        return string

    def order_bfs(self) -> List[Node]:
        """
        Genera una lista de los nodos ordenados por amplitud.

        :return: Una lista de nodos ordenados por amplitud
        """
        pending: List[Node] = [self.root]
        nodelist: List[Node] = []

        while pending:
            curr = pending.pop(0)
            nodelist.append(curr)

            for child in curr.children:
                pending.append(child)
        
        return nodelist

    def _assign_code_char(self, code_dict, node, code):
        """
        Función auxiliar recursiva de to_code_dict

        Si encuentra un nodo con un carácter, devuelve el código generado hasta el momento. Si encuentra un nodo de
        conexión, se llama a sí misma usando los hijos del nodo, aumentando el código según la posición del hijo.

        :param code_dict: El diccionario al que se agregan los códigos (se modifica por referencia)
        :param node: El nodo por analizar
        :param code: El código hasta el momento
        """

        if node.char:
            # Si es un nodo con un carácter, modificar el diccionario con el código hasta el momento
            code_dict[node.char] = code
        
        if len(node.children) == 2:
            # Si es un nodo de conexión, llamarse a sí misma con cada uno de sus hijos, agregando al código un 0 si es
            # el hijo izquierdo y un 1 si es el hijo derecho (arbitrario)
            self._assign_code_char(code_dict, node.children[0], code + '0')
            self._assign_code_char(code_dict, node.children[1], code + '1')

    def to_code_dict(self) -> Dict[str, str]:
        """
        Convierte el árbol a un diccionario de códigos basándose en su posición en el árbol.

        :return: Un diccionario de códigos en formato "carácter": "código"
        """

        # Si sólo hay un nodo en el árbol, representarlo con un 0
        if not self.root.children:
            return {self.root.char: '0'}
        
        code_dict = {}

        # Asignar recursivamente los códigos a cada carácter
        self._assign_code_char(code_dict, self.root, '')

        return code_dict
