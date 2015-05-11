#qpy:kivy

from kivy import require
require("1.8.0")

from kivy.app import App

from kivy.lang import Builder

from kivy.uix.button import Button

from random import random

class ButtonNewClass(Button) :
	def on_press(self) :
		self.text = "Pressed"
		rgbaColors = []
		for i in range(3) :
			rgbaColors.append(random())
		rgbaColors.append(1.0)
		print(rgbaColors)
		self.background_color = rgbaColors
		print("Click on " + str(self.name) + "!")

firstBuilder = Builder.load_string("""
#kivy 1.8.0
<ButtonNewClass>:
	bold: True
	font_size: 30
	size_hint: (0.5, 0.25)
FloatLayout:
	ButtonNewClass:
		name: "1"
		background_color: (1, 0, 0, 0.5)
		pos_hint: {"x": 0.0, "y": 0.75}
		text: "Button1"
	ButtonNewClass:
		name: "2"
		background_color: (0, 1, 0, 0.5)
		pos_hint: {"x" : 0.50, "y": 0.75}
		text: "Button2"
	ButtonNewClass:
		name: "3"
		background_color: (0, 0, 1, 0.5)
		pos_hint: {"x" : 0.0, "y": 0.0}
		text: "Button3"
	ButtonNewClass:
		name: "4"
		background_color: (1, 0, 1, 1)
		pos_hint: {"x" : 0.50, "y": 0.0}
		text: "Button4"
	ButtonNewClass:
		name: "0"
		background_color: (0, 0, 0, 1)
		pos_hint: {"x" : 0, "y" : 0.25}
		size_hint: (1, 0.5)
		text: "Main Button"
""")

class First_newApp(App) :
	def build(self) :
		return(firstBuilder)

if(__name__ == "__main__") :
	First_newApp().run()