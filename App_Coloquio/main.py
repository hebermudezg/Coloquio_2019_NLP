from kivy.app import App  #libreria principal
from kivymd.theming import ThemeManager


class MainApp(App):
    theme_cls = ThemeManager()

    




MainApp().run()  # corriendo aplicación