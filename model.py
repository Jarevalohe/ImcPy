class Model:
    def __init__(self):
        self.weight = 0
        self.height = 0
        self.result = 0
        self.resultType = ""

    def setWeight(self, weight):
        self.weight = weight

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height
        
    def getWeight(self):
        return self.weight
        
    def getResult(self, weight, height):
        self.result = (float(weight) / pow(float(height),2))
        if(self.result<18.5):
            self.resultType="Bajo peso"
        elif (self.result>18.5 and self.result<24.9):
            self.resultType="Peso normal"
        elif (self.result>25.0 and self.result<29.9):
            self.resultType="Sobre peso"
        elif (self.result>30.0 and self.result<34.9):
            self.resultType="Obesidad grado 1"
        elif (self.result>35.0 and self.result<39.9):
            self.resultType="Obesidad grado 2"
        else:
            self.resultType="Obesidad grado 3, Obesidad mórbida"
        print("Su IMC es -> ",self.result)
        print(self.resultType)