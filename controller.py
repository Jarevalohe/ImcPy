from model import Model
from view import View

class Controller:
    def __init__(self):
        self.objView = View()
        self.objModel = Model()

    def run(self):
        self.objModel.setWeight(self.objView.weight)
        self.objModel.setHeight(self.objView.height)
        self.objModel.getResult(self.objModel.weight,self.objModel.height)


controller = Controller()
controller.run()