#coding: utf-8
# imporatendo bibliotecas
from kivy.app import App
from kivy.uix.label import Label

#creando funcion
def build():
    return Label(text="Hello world")
    



hello_world = App()
hello_world.build = build
hello_world.run()

#App().run() #clase app