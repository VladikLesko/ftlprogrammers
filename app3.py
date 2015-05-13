#qpy:kivy
from kivy import require
require("1.8.0")

from kivy.app import App

from kivy.clock import Clock

from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.lang import Builder

from random import randint
from time import sleep
from threading import Thread

Builder.load_string("""
#:kivy 1.8.0
<MainButtonClass>:
	bold: True
	font_size: 30

<LoadingWindow>:
	name: "LoadingWindow"
	FloatLayout:
		Label:
			font_size: 35
			text: "Loading..."
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0.01, "y": 0.01}
			background_color: (0, 0, 0, 0)
		Image:
			size_hint: (0.2, 0.2)
			pos_hint: {"x": 0.79, "y": 0.01}
			source: "textures/loadingimage.png"

<MainWindow>:
	name: "MainWindow"
	FloatLayout:
		MainButtonClass:
			text: "Exit"
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0.05, "y": 0.05}
			background_color: (0, 0, 0, 0)
			on_press:
				from os import _exit
				exit(0)
		MainButtonClass:
			text: "To settings"
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0.7, "y": 0.05}
			background_color: (0, 0, 0, 0)
			on_press:
				root.manager.transition.direction = root.get_random_direction()	
				root.manager.current = "SettingsWindow"

<SettingsWindow>:
	name: "SettingsWindow"
	FloatLayout:
		MainButtonClass:
			text: "Return"
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0.7, "y": 0.05}
			background_color: (0, 0, 0, 0)
			on_press:
				root.manager.transition.direction = root.get_random_direction()
				root.manager.current = "MainWindow"
""")

class MainButtonClass(Button) :
	pass

lastDirection = ""
class MainScreenClass(Screen) :
	def get_random_direction(self) :
		global lastDirection
		directions = ("up", "down", "left", "right")
		newDirection = ""
		while((lastDirection == newDirection) or (newDirection == "")) :
			newDirection = directions[randint(0, 3)] 
		lastDirection = newDirection
		return(newDirection)

class LoadingWindow(MainScreenClass) :
	pass

class MainWindow(MainScreenClass) :
	pass

class SettingsWindow(MainScreenClass) :
	pass

MainScreenManager = ScreenManager()
MainScreenManager.add_widget(LoadingWindow())
MainScreenManager.add_widget(MainWindow())
MainScreenManager.add_widget(SettingsWindow())
MainScreenManager.current = "LoadingWindow"

def SetMainScreen(dt) :
	MainScreenManager.current = "MainWindow"

Clock.schedule_once(SetMainScreen, 2.5)

class GameApp(App) :
	def build(self) :
		return(MainScreenManager)

if(__name__ == "__main__") :
	GameApp().run()