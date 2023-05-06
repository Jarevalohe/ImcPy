from model import Model


class Controller:
    def Calcular(weight, height):
        objModel = Model()
        objModel.setWeight(weight)
        objModel.setHeight(height)
        return objModel.getResult(weight,height)


