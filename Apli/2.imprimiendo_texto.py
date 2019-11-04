#coding: utf-8

from kivy.app import App  # importanod clase App 
from kivy.uix.label import Label # importando clase Label

def build():
    lb = Label()
    lb.text="Curso de Python y kivy"
    lb.italic = True
    lb.font_size = 50
    return lb


app = App()
app.build = build
app.run() # ejecutar la app run contenida en App