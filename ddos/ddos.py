#qpy:kivy
from kivy import require
require("1.8.0")

from kivy.lang import Builder
BuildDDos = Builder.load_string("""
#:kivy 1.8.0
FloatLayout:
	Label:
		text: "Yotson's DDos App"
		font_size: 36
		size_hint: (1, 0.1)
		pos_hint: {"x": 0,"y": 0}
""")

from kivy.app import App

class DDosApp(App) :
	def build(self) :
		return(BuildDDos)

if(__name__ == "__main__") :
	DDosApp().run()