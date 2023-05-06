import pytest
from model import Model

def test_setWeight():
    objModel = Model()
    objModel.setWeight(70)
    assert objModel.weight == 70   # Se busca verificar que el peso se haya asignado correctamente

def test_setHeight():
    objModel = Model()
    objModel.setHeight(1.8)
    assert objModel.height == 1.8  # Se busca verificar que la altura se haya asignado correctamente

def test_getResult_bajoPeso():
    objModel = Model()
    result = objModel.getResult(50, 1.8)
    assert result == "Bajo peso su IMC es \n15.4" # Se busca verificar que el resultado y la categoría sean correctos

def test_getResult_pesoNormal():
    objModel = Model()
    result = objModel.getResult(70, 1.8)
    assert result == "Peso normal su IMC es \n21.6" # Se busca verificar que el resultado y la categoría sean correctos

def test_getResult_sobrePeso():
    objModel = Model()
    result = objModel.getResult(85, 1.8)
    assert result == "Sobre peso su IMC es \n26.2" # Se busca verificar que el resultado y la categoría sean correctos

def test_getResult_obesidadGrado1():
    objModel = Model()
    result = objModel.getResult(100, 1.8)
    assert result == "Obesidad grado 1 su IMC es \n30.9" # Se busca verificar que el resultado y la categoría sean correctos

def test_getResult_obesidadGrado2():
    objModel = Model()
    result = objModel.getResult(120, 1.8)
    assert result == "Obesidad grado 2 su IMC es \n37.0" # Se busca verificar que el resultado y la categoría sean correctos

def test_getResult_obesidadGrado3():
    objModel = Model()
    result = objModel.getResult(150, 1.8)
    assert result == "Obesidad grado 3, Obesidad mórbida su IMC es \n46.3" # Se busca verificar que el resultado y la categoría sean correctos

def test_getResult_invalidInput():
    objModel = Model()
    with pytest.raises(ValueError):  # Se busca verificar si existe una excepción controlada si se ingresan valores inválidos
        objModel.getResult(0, 0)
        objModel.getResult(-70, 1.8)
        objModel.getResult(70, -1.8)
        objModel.getResult("70", "1.8")
