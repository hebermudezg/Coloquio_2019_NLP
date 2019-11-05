from kivy.app import App  #libreria principal
from kivymd.theming import ThemeManager

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')

class MainApp(App):
    theme_cls = ThemeManager()


MainApp().run()  # corriendo aplicación