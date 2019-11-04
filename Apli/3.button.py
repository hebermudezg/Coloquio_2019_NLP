#coding: utf-8

from kivy.app import App  # importanod clase App 
from kivy.uix.label import Label # importando clase Label
from kivy.uix.button import Button

def click():
    print("El boton fue presionado")


def build():
    bt = Button()
    bt.text = "Clic"
    bt.on_press = click # evento click de la clase button
    return (bt)



app = App()
app.build = build
app.run() # ejecutar la app run contenida en App