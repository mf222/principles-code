class Notebook():

    def __init__(self):
        self.pages = dict()
        self.actual_page = 0

    def write_page(self, data):
        self.pages[self.actual_page] = data
        self.actual_page += 1
        for number, page in self.pages.items():
            self.pages[number] = page + "This was page {}".format(number)
        return self.pages
