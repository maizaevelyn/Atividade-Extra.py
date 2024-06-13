from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.modalview import ModalView
from functools import partial


class Login(BoxLayout):
    def __init__(self, arg1=None, arg2=None, **kwargs):
        Window.clearcolor = get_color_from_hex("#80008e")
        super().__init__(**kwargs)
        self.arg1 = arg1
        self.arg2 = arg2
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        self.add_widget(Label(text="Faça seu Cadastro", font_size=40, font_name='Georgia', color=get_color_from_hex('#ff99cc')))

        self.username_input = TextInput(hint_text="Digite seu Email ...", foreground_color=get_color_from_hex('#ff99cc'))
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True, foreground_color=get_color_from_hex('#ff99cc'))

        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#ff99cc'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#ff99cc'), font_size=20))
        self.add_widget(self.senha_input)

        self.cadastrar_button = Button(text="Entrar", background_color=get_color_from_hex('#80008e'), color=get_color_from_hex('#ff99cc'))
        self.cadastrar_button.bind(on_release=partial(self.create_new_window, self.arg1, self.arg2))

        self.add_widget(self.cadastrar_button)

    def create_new_window(self, arg1, arg2, instance):
        new_window = NewWindow(arg1, arg2)
        new_window.open()
        Window.clearcolor = get_color_from_hex("#80008e")

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()


class NewWindow(BoxLayout):
    def __init__(self, arg1, arg2, **kwargs):
        Window.clearcolor = get_color_from_hex("#80008e")
        super().__init__(**kwargs)
        self.arg1 = arg1
        self.arg2 = arg2
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('#ff99cc')))

        self.email_input = TextInput(hint_text="Digite seu email ...", foreground_color=get_color_from_hex('#ff99cc'))
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True, foreground_color=get_color_from_hex('#ff99cc'))

        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#ff99cc'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#ff99cc'), font_size=20))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=get_color_from_hex('#80008e'), color=get_color_from_hex('#ff99cc'))
        self.button_cadastrar.bind(on_release=partial(self.entrar_interface_login, self.arg1, self.arg2))

        self.add_widget(self.button_cadastrar)

    def entrar_interface_login(self, arg1, arg2, instance):
        entrar_login = Login(arg1, arg2)
        entrar_login.open()
        Window.clearcolor = get_color_from_hex("#80008e")

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()


class MyApp(App):
    def build(self):
        return Login()


if __name__ == '__main__':
    MyApp().run()
