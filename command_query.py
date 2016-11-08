class Notebook():
    def __init__(self):
        self.pages = dict()
        self.actual_page = 0

    def write_page(self, data):
        self.pages[self.actual_page] = data
        self.actual_page += 1

    def get_pages(self):
        return self.pages
