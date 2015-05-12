#qpy:kivy

from kivy import require
require("1.8.0")

from kivy.app import App

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
#:kivy 1.8.0
<MainScreen>:
	name: "main"
	Button:
		text: "To settings!"
		background_color: (1, 0, 0, 1)
		bold: True
		on_press:
			root.manager.transition.direction = "left"
			root.manager.current = "nomain"
<NoMainScreen>:
	name: "nomain"
	Button:
		text: "Return to main screen!"
		background_color: (0, 1, 0, 1)
		bold: True
		on_press:
			root.manager.transition.direction = "right"
			root.manager.current = "main"
""")

class MainScreen(Screen) :
	pass

class NoMainScreen(Screen) :
	pass

MainScreenManager = ScreenManager()
MainScreenManager.add_widget(MainScreen())
MainScreenManager.add_widget(NoMainScreen())

class MainApp(App) :
	def build(self) :
		return(MainScreenManager)

if(__name__ == "__main__") :
	MainApp().run()