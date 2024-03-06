'''
Classe que representa uma certa possição no ambiente
'''

class Estado:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"