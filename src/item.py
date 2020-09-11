class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f'\n-------------------------------------------------------------------\n\n !!! You have picked up a {self.name} !!!\n')
    def on_drop(self):
        print(f'\n-------------------------------------------------------------------\n\n !!! You have dropped a {self.name} !!!\n')