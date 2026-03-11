from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):

    def build(self):
        self.expression = ""

        layout = GridLayout(cols=1)

        self.display = TextInput(
            text="",
            readonly=True,
            font_size=40,
            halign="right",
            size_hint=(1,0.2)
        )

        layout.add_widget(self.display)

        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0",".","C","+"]
        ]

        for row in buttons:
            row_layout = GridLayout(cols=4)

            for label in row:
                btn = Button(text=label, font_size=30)
                btn.bind(on_press=self.on_button_press)
                row_layout.add_widget(btn)

            layout.add_widget(row_layout)

        equals = Button(text="=", font_size=35, size_hint=(1,0.2))
        equals.bind(on_press=self.calculate)

        layout.add_widget(equals)

        return layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.expression = ""
        else:
            self.expression += text

        self.display.text = self.expression

    def calculate(self, instance):
        try:
            result = str(eval(self.expression))
            self.display.text = result
            self.expression = result
        except:
            self.display.text = "Error"
            self.expression = ""

CalculatorApp().run()