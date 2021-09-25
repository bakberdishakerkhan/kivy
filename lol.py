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
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        h1 = BoxLayout()
        txt = Label(text= 'Выбери экран')
        v1.add_widget(ScrButton(self, direction='down',goal='first', text='1'))
        v1.add_widget(ScrButton(self, direction='left',goal='second', text='2'))
        v1.add_widget(ScrButton(self, direction='up',goal='third', text='3'))
        v1.add_widget(ScrButton(self, direction='right',goal='fourth', text='4'))
        h1.add_widget(txt)
        h1.add_widget(v1)
        self.add_widget(h1)
class FirstScr(Screen):
    def  __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x':0.5, 'center_y':0.5})
        btn = Button(text='Выбор: 1', size_hint=(.10, .8), pos_hint={'left':0})
        btn_back = ScrButton(self, direction='up', goal='main', text='Назад', size_hint=(.5, 1), pos_hint={'rigth':1})
        v1.add_widget(btn)
        v1.add_widget(btn_back)
        slef.add_widget(v1)
class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation='vertical')
        self.txt = Label(text= 'Выбор: 2')
        v1.add_widget(self.txt)

        h1_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl1 = Label(text='Введите пароль:', halign='right')
        self.input = TextInput(multiline=False)

        h1_0.add_widget(lbl1)
        h1_0.add_widget(self.input)
        v1.add_widget(h1_0)

        h1 = BoxLayout(size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        btn_false = Button(text='OK!')
        btn_back = ScrButton(self, direction='right', goal='main', text='Назад')

        h1.add_widget(btn_false)
        h1.add_widget(btn_back)
        v1.add_widget(h1)
        self.add_widget(v1)
        btn_false.on_press = self.change_text
    def change_text(self):
        self.txt.text = self.input.text + '? Не сработало ...'
class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        btn_back = ScrButton(self, direction='down', goal='main', text='Назад', size_hint=(1, None), height='40sp')
        test_label = Label(text= "Твой собственный экран")
        layout.add_widget(test_label)
        layout.add_widget(btn_back)
        self.add_widget(layout)

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation='vertical', spacing=8)
        a = 'START' + 'Выбор: 3' * 200
        test_label = Label(text = 'Дополнительное задание',size_hint=(0.3, None))

        btn_back = ScrButton(self, direction='left', goal='main', text='Назад', size_hint=(1, .2), pos_hint={'center-x':0.5})
        self.label = Label(text=a, size_hint_y=None, font_size='24sp', halign='left', valign='top')
        self.label.bind(size=self.resize)
        self.scroll = ScrollView(size_hint=(1, 1))
        self.scroll.add_widget(self.label)

        v1.add_widget(test_label)
        v1.add_widget(btn_back)
        v1.add_widget(self.scroll)
        self.add_widget(v1)
    def resize(self, *args):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]
    
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm
MyApp().run()
