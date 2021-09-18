#не забудь импортировать необходимые элементы!
from kivy.app import App 
from kivy.ulx.label import Label
from kivy.ulx.button import Button 
from kivy.ulx.textinput import TextInput 
from kivy.ulx.boxlayout import BoxLayout 
from kivy.ulx.screenmanager import ScreenManager, Screen 
from kivy.ulx.scrollview import ScrollView 
class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScr(Screen):
    def __init__(self, **kwargs):
