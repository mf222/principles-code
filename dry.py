class List():
    def __init__(self):
        self.lista = []

    def find(self, e):
        for element in self.lista:
            if element == e:
                return element

    def append(self, element):
        self.lista.append(element)

    def increase(self, e):
        find(e) += 1

    def decrease(self, e):
        find(e) -= 1

    def duplicate(self, e):
        find(e) *= 2
