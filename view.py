class View:
        def _init_(self) -> None:
            self.weight = 0
            self.height = 0   
            print("Ingrese su peso en kilogramos")
            self.weight = input()
            print("Ingrese su altura en metros")
            self.height = input()