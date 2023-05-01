class View:
    def __init__(self):
        self.weight = 0
        self.height = 0   
        print("Ingrese su peso en kilogramos")
        self.weight = float(input())
        print("Ingrese su altura en metros")
        self.height = float(input())