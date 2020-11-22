from kivy.app import App
from kivy.extras.highlight import KivyLexer
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.behaviors import EmacsBehavior
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
from pygments import lexers
import codecs
import os

initial_code = '''
OwO

function masUno int x : int {
    return x + 1;
}

function cero : int {
    return 0;
}


# int x = masUno(1); Esto causa un error
int zero = cero();
int x = masUno(1);
'''

class Fnt_SpinnerOption(SpinnerOption):
    pass


class LoadDialog(Popup):

    def load(self, path, selection):
        self.choosen_file = [None, ]
        self.choosen_file = selection
        Window.title = selection[0][selection[0].rfind(os.sep) + 1:]
        self.dismiss()

    def cancel(self):
        self.dismiss()


class SaveDialog(Popup):

    def save(self, path, selection):
        _file = codecs.open(selection, 'w', encoding='utf8')
        _file.write(self.text)
        Window.title = selection[selection.rfind(os.sep) + 1:]
        _file.close()
        self.dismiss()

    def cancel(self):
        self.dismiss()


class CodeInputWithBindings(EmacsBehavior, CodeInput):
    '''CodeInput with keybindings.
    To add more bindings, add the behavior before CodeInput in the class
    definition.
    '''
    pass


class CodeInputTest(App):

    files = ListProperty([None, ])

    def build(self):
        b = BoxLayout(orientation='vertical')
        languages = Spinner(
            text='language',
            values=sorted(['KvLexer', ] + list(lexers.LEXERS.keys())))

        languages.bind(text=self.change_lang)

        menu = BoxLayout(
            size_hint_y=None,
            height='30pt')
        fnt_size = Spinner(
            text='12',
            values=list(map(str, list(range(5, 40)))))
        fnt_size.bind(text=self._update_size)

        fonts = [
            file for file in LabelBase._font_dirs_files
            if file.endswith('.ttf')]

        fnt_name = Spinner(
            text='RobotoMono',
            option_cls=Fnt_SpinnerOption,
            values=fonts)
        fnt_name.bind(text=self._update_font)
        mnu_file = Spinner(
            text='File',
            values=('Open', 'SaveAs', 'Save', 'Close'))
        mnu_file.bind(text=self._file_menu_selected)
        key_bindings = Spinner(
            text='Key bindings',
            values=('Default key bindings', 'Emacs key bindings'))
        key_bindings.bind(text=self._bindings_selected)

        menu.add_widget(mnu_file)
        menu.add_widget(fnt_size)
        menu.add_widget(fnt_name)
        menu.add_widget(languages)
        menu.add_widget(key_bindings)
        b.add_widget(menu)

        self.codeinput = CodeInputWithBindings(
            lexer=KivyLexer(),
            font_size=12,
            text=initial_code,
            key_bindings='default',
        )

        self.output_box = CodeInputWithBindings(
            font_size=12,
            text="SECTION: Input/Output",
            key_bindings='default',
        )

        self.command_input = TextInput(text='Hello world', multiline=False, cursor_blink=True, cursor_width=8)
        self.command_input.bind(on_text_validate=self.on_enter)

        b.add_widget(self.codeinput)
        b.add_widget(self.output_box)
        b.add_widget(self.command_input)

        return b

    def on_enter(self, instance):
      self.stdin = instance.text
      self.display_output(self.stdin) 

    def get_code(self):
      return self.codeinput.text

    def display_output(self, message):
      output = f'\n{message}'
      print(f'STDOUT: {output}') 
      self.output_box.text += output

    def _update_size(self, instance, size):
        self.codeinput.font_size = float(size)

    def _update_font(self, instance, fnt_name):
        instance.font_name = self.codeinput.font_name = fnt_name

    def _file_menu_selected(self, instance, value):
        if value == 'File':
            return
        instance.text = 'File'
        if value == 'Open':
            if not hasattr(self, 'load_dialog'):
                self.load_dialog = LoadDialog()
            self.load_dialog.open()
            self.load_dialog.bind(choosen_file=self.setter('files'))
        elif value == 'SaveAs':
            if not hasattr(self, 'saveas_dialog'):
                self.saveas_dialog = SaveDialog()
            self.saveas_dialog.text = self.codeinput.text
            self.saveas_dialog.open()
        elif value == 'Save':
            if self.files[0]:
                _file = codecs.open(self.files[0], 'w', encoding='utf8')
                _file.write(self.codeinput.text)
                _file.close()
        elif value == 'Close':
            if self.files[0]:
                self.codeinput.text = ''
                Window.title = 'untitled'

    def _bindings_selected(self, instance, value):
        value = value.split(' ')[0]
        self.codeinput.key_bindings = value.lower()

    def on_files(self, instance, values):
        if not values[0]:
            return
        _file = codecs.open(values[0], 'r', encoding='utf8')
        self.codeinput.text = _file.read()
        _file.close()

    def change_lang(self, instance, z):
        if z == 'KvLexer':
            lx = KivyLexer()
        else:
            lx = lexers.get_lexer_by_name(lexers.LEXERS[z][2][0])
        self.codeinput.lexer = lx



if __name__ == '__main__':
    CodeInputTest().run()
