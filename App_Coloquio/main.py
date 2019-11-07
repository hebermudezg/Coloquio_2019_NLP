import kivy
from kivy.app import App  #libreria principal
from kivymd.theming import ThemeManager

# importaciones
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainApp(App):
    theme_cls = ThemeManager()
    #def build(self):
       # return Button(text="Ok")

MainApp().run()  # corriendo aplicación.