# https://open.kattis.com/problems/bst
import sys


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent  # Added in order to delete a node easier
        self.left = None
        self.right = None
    
    def __repr__(self):
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def empty(self):
        return self.root is None
    
    def __str__(self):
        """
        Return a string of all the Nodes using in order traversal
        """
        return str(self.root)

    def insert(self, value):
        node = Node(value, None)
        if self.empty(): # si l'arbre est vide
            self.root = node
            return 0
        else:
            # on part du parent
            parent = self.root
            depth = 1
            while True: #tant qu'on n'arrive pas à insérer notre noeud
                if parent.value < node.value: #go right
                    if parent.right is None:
                        parent.right = node #on insère le noeud
                        break
                    else:
                        parent = parent.right #on descend à droite
                else: #go left
                    if parent.left is None:
                        parent.left = node #on insère le noeud
                        break
                    else:
                        parent = parent.left #on descend à gauche
                depth += 1
            node.parent = parent #on update le parent de notre noeud
            return depth



def solution():
    n = int(input())
    tree = BinarySearchTree()
    C = 0
    for line in sys.stdin:
        a = int(line.rstrip("\n"))
        C += tree.insert(a)
        sys.stdout.write(f"{C}\n")


solution()
