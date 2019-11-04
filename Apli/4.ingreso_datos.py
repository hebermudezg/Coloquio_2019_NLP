
from kivy.app import App
from kivy.uix.textinput import TextInput # Entrada de tecto

def build():
    return TextInput(text="Ejemplo de texto")  # Caja de texto. 

janela =App()
janela.build = build
janela.run()