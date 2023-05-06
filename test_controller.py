from model import Model
from controller import Controller

def test_imc_bajo_peso():
    # Verificar que se devuelve el resultado esperado para una persona con IMC de bajo peso (17.3)
    assert Controller.Calcular(50, 1.7) == "Bajo peso su IMC es \n17.3"

def test_imc_peso_normal():
    # Verificar que se devuelve el resultado esperado para una persona con IMC de peso normal (22.2)
    assert Controller.Calcular(68, 1.75) == "Peso normal su IMC es \n22.2"

def test_imc_sobre_peso():
    # Verificar que se devuelve el resultado esperado para una persona con IMC de sobre peso (27.7)
    assert Controller.Calcular(80, 1.7) == "Sobre peso su IMC es \n27.7"

def test_imc_obesidad_grado_1():
    # Verificar que se devuelve el resultado esperado para una persona con IMC de obesidad grado 1 (34.6)
    assert Controller.Calcular(100, 1.7) == "Obesidad grado 1 su IMC es \n34.6"

def test_imc_obesidad_grado_2():
    # Verificar que se devuelve el resultado esperado para una persona con IMC de obesidad grado 2 (38.1)
    assert Controller.Calcular(112, 1.7) == "Obesidad grado 2 su IMC es \n38.8"

def test_imc_obesidad_grado_3():
    # Verificar que se devuelve el resultado esperado para una persona con IMC de obesidad grado 3 (51.9)
    assert Controller.Calcular(150, 1.7) == "Obesidad grado 3, Obesidad mórbida su IMC es \n51.9"
