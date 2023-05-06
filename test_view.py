from tkinter import *
from view import View
import pytest

class TestView:
    @pytest.fixture
    def app(self):
        view = View()
        return view

    def test_app_exists(self, app): #Se verifica que se genere la ventana correctamente
        assert app is not None
        assert isinstance(app, View)
        
