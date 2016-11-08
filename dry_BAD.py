class List():
    def __init__(self):
        self.lista = []

    def append(self, element):
        self.lista.append(element)

    def increase(self, e):
        for element in self.lista:
            if e == element:
                element += 1

    def decrease(self, e):
        for element in self.lista:
            if e == element:
                element -= 1

    def duplicate(self, e):
        for element in self.lista:
            if e == element:
                element *= 2
