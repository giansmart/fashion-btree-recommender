import os
import pickle
import math
import numpy as np

BASE_PATH = "temp"

class BTreeNode:
    def __init__(self, id, is_leaf=False):
        self.id = id  # Identificador único del nodo
        self.is_leaf = is_leaf  # Indica si el nodo es hoja
        self.keys = []  # Lista de tuplas (product_id, feature_vector)
        self.children = []  # Lista de identificadores de hijos

class BTree:
    def __init__(self, degree):
        self.root = BTreeNode(0, True)  # Inicializa la raíz como una hoja
        self.t = math.ceil(degree / 2)  # Grado mínimo del árbol
        self.next_id = 1  # Para asignar IDs únicos a los nodos
        self._len = 0

    def __iter__(self):
        """Hacer que el árbol sea iterable."""
        stack = [self.root]
        while stack:
            node = stack.pop()
            yield from node.keys # Devolver la clave de cada nodo
            if not node.is_leaf:
                stack.extend(self._load_node(child_id) for child_id in reversed(node.children))
    
    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def insert(self, product_id, feature_vector):
        """Insertar una tupla (product_id, feature_vector) en el Árbol B."""
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:  # Si la raíz está llena
            new_root = BTreeNode(self.next_id)
            self.next_id += 1
            new_root.children.append(self.root.id)  # Antiguo nodo raíz como hijo
            self._split_child(new_root, 0)  # Dividir el primer hijo
            self.root = new_root  # Actualizar la raíz
        self._insert_non_full(self.root, product_id, feature_vector)
        self._save_node(self.root)  # Guardar la nueva raíz
        self._len += 1

    def _split_child(self, parent, index):
        """Dividir un hijo lleno en dos nodos."""
        t = self.t
        child = self._load_node(parent.children[index])
        new_child = BTreeNode(self.next_id, child.is_leaf)
        self.next_id += 1

        # Mover la clave del medio al padre
        parent.keys.insert(index, child.keys[t - 1])

        # Asignar las claves y los hijos al nuevo nodo
        new_child.keys = child.keys[t:(2 * t) - 1]
        child.keys = child.keys[0:t - 1]

        if not child.is_leaf:
            new_child.children = child.children[t:(2 * t)]
            child.children = child.children[0:t]

        # Insertar el nuevo nodo como hijo del padre
        parent.children.insert(index + 1, new_child.id)

        # Guardar los nodos en disco
        self._save_node(child)
        self._save_node(new_child)
        self._save_node(parent)

    def _insert_non_full(self, node, product_id, feature_vector):
        """Insertar una tupla en un nodo que no está lleno."""

        index = len(node.keys) - 1

        # Insertar en un nodo hoja
        if node.is_leaf:
            while index >= 0 and product_id < node.keys[index][0]:
                index -= 1
            node.keys.insert(index + 1, (product_id, feature_vector))
            self._save_node(node)
        else:
            # Buscar el hijo adecuado para descender
            while index >= 0 and product_id < node.keys[index][0]:
                index -= 1
            index += 1
            child = self._load_node(node.children[index])

            # Si el hijo está lleno, dividirlo
            if len(child.keys) == (2 * self.t) - 1:
                self._split_child(node, index)
                if product_id > node.keys[index][0]:
                    index += 1

            self._insert_non_full(self._load_node(node.children[index]), product_id, feature_vector)

    def search(self, product_id, node=None):
        """Buscar un product_id en el Árbol B y devolver la tupla completa."""
        if node is None:
            node = self.root  # Comenzar desde la raíz

        index = 0
        while index < len(node.keys) and product_id > node.keys[index][0]:
            index += 1

        if index < len(node.keys) and product_id == node.keys[index][0]:
            return node.keys[index]  # Devolver la tupla encontrada
        elif node.is_leaf:
            return None  # No encontrado
        else:
            return self.search(product_id, self._load_node(node.children[index]))

    def _save_node(self, node):
        """Guardar el nodo en un archivo binario usando pickle."""
        if not os.path.exists(BASE_PATH):
            os.makedirs(BASE_PATH)
        with open(f"{BASE_PATH}/btree_node_{node.id}.pkl", 'wb') as file:
            pickle.dump(node, file)

    def _load_node(self, id):
        """Cargar un nodo desde un archivo binario usando pickle."""
        with open(f"{BASE_PATH}/btree_node_{id}.pkl", 'rb') as file:
            return pickle.load(file)

    def print_tree(self, node=None, level=0):
      """Imprimir el Árbol B en forma jerárquica con nombres de archivos."""
      if node is None:
          node = self.root  # Empezar desde la raíz

      # Obtener el nombre del archivo del nodo actual
      filename = f"{BASE_PATH}/btree_node_{node.id}.pkl"

      indent = "  " * level  # Indentación para niveles
      print(f"{indent}Nodo (Archivo: {filename}):")
      print(f"{indent}  Claves: {node.keys}")

      if not node.is_leaf:  # Si el nodo tiene hijos, imprimirlos
          print(f"{indent}  Hijos:")
          for child_id in node.children:
              child_filename = f"{BASE_PATH}/btree_node_{child_id}.pkl"
              print(f"{indent}    {child_filename}")
              # Cargar el nodo hijo y continuar la impresión recursivamente
              child_node = self._load_node(child_id)
              self.print_tree(child_node, level + 1)

    def print_tree_simple(self):
        """Imprimir el Árbol B de manera simple."""
        for node in self.root:
            print(node)

btree = BTree(3)

btree.insert(5, [0.1, 0.2, 0.3])
btree.insert(3, [0.4, 0.5])
btree.insert(20, [0.6, 0.7])
btree.insert(13, [0.8, 0.9])
btree.insert(8, [1.0, 1.1])
btree.insert(55, [1.2, 1.3])
btree.insert(12, [1.2, 1.3])
btree.insert(0, [1.2, 1.3])

# btree.print_tree()
#btree.print_tree_simple()
# !rm *.pkl