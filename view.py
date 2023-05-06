from tkinter import *
from controller import Controller
class View:
    def __init__(self):
        objControlador= Controller()
        raiz = Tk()
        frame = Frame(raiz, width=600,height=400)
        frame.pack()
        weightLabel= Label(frame,text="Ingrese su peso").place(x=200,y=100)
        weightText= Entry(frame)
        weightText.place(x=300, y=100)
        heightLabel= Label(frame,text="Ingrese su altura").place(x=200,y=130)
        heightText= Entry(frame)
        heightText.place(x=300, y=130)
        resultLabel= Label(frame,text="Resultado").place(x=200,y=150)
        resultValueLabel= Label(frame,text="Resultado").place(x=200,y=150)
        def calculate():
            result= Controller.Calcular(float(weightText.get()),float(heightText.get()))
            Label(frame,text=result).place(x=300,y=150)

        Button(frame,text="Calcular",command=calculate).place(x=280,y=190)
        
        raiz.mainloop()

        
        