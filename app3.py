#qpy:kivy
from kivy import require
require("1.8.0")

from kivy.app import App

from kivy.clock import Clock

from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.lang import Builder

from random import randint, random
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
			bold: True
			font_size: 35
			text: "Loading..."
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0.01, "y": 0.01}
			background_color: (0, 0, 0, 0)

<MainWindow>:
	name: "MainWindow"
	FloatLayout:
		MainButtonClass:
			text: "Exit"
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0, "y": 0.025}
			background_color: (0, 0, 0, 0)
			on_press:
				from os import _exit
				exit(0)
		MainButtonClass:
			text: "To settings"
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0.7, "y": 0.025}
			background_color: (0, 0, 0, 0)
			on_press:
				root.manager.transition.direction = root.get_random_direction()	
				root.manager.current = "SettingsWindow"
		ToGameButtonClass:
			text: "Play"
			bold: True
			font_size: 70
			size_hint: (0.5, 0.5)
			pos_hint: {"x": 0.25, "y": 0.25}
			background_color: (0, 0, 0, 0)

<SettingsWindow>:
	name: "SettingsWindow"
	FloatLayout:
		Label:
			text: "No settings!"
			font_size: 70
			bold: True
			size_hint: (0.5, 0.5)
			pos_hint: {"x": 0.25, "y": 0.25}
			background_color: (0, 0, 0, 0)
		MainButtonClass:
			text: "Return"
			size_hint: (0.25, 0.1)
			pos_hint: {"x": 0.75, "y": 0.025}
			background_color: (0, 0, 0, 0)
			on_press:
				root.manager.transition.direction = root.get_random_direction()
				root.manager.current = "MainWindow"
<RandomButton>:
	text: "0"
	bold: True
	font_size: 20
	background_color: self.GetRandomColor()
<GameWindow>:
	name: "GameWindow"
	MainButtonClass:
		text: "Stop game"
		size_hint: (0.25, 0.1)
		font_size: 40
		pos_hint: {"x": 0.7, "y": 0.85}
		background_color: (0, 0, 0, 0)
		on_press:
			root.manager.transition.direction = root.get_random_direction()
			root.manager.current = "MainWindow"
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.05, "y": 0.05}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.35, "y": 0.05}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.65, "y": 0.05}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.05, "y": 0.3}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.35, "y": 0.3}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.65, "y": 0.3}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.05, "y": 0.55}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.35, "y": 0.55}
	RandomButton:
		size_hint: (0.3, 0.25)
		pos_hint: {"x": 0.65, "y": 0.55}
""")

class MainButtonClass(Button) :
	pass

def GetRandomColor(self) :
	rgbaColor = []
	for i in range(3) :
		rgbaColor.append(random())
	rgbaColor.append(1)
	return(rgbaColor)

class RandomButton(Button) :
	def GetRandomColor(self) :
		rgbaColor = []
		for i in range(3) :
			rgbaColor.append(random())
		rgbaColor.append(1)
		return(rgbaColor)
	def on_press(self) :
		self.text = str(int(self.text) + 1)
		self.background_color = self.GetRandomColor()

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

class GameWindow(MainScreenClass) :
	pass

MainScreenManager = ScreenManager()

class ToGameButtonClass(Button) :
	def on_press(self) :
		MainScreenManager.current = "LoadingWindow"
		def SetGameScreen(dt) :
			MainScreenManager.current = "GameWindow"
		Clock.schedule_once(SetGameScreen, 1)

MainScreenManager.add_widget(LoadingWindow())
MainScreenManager.add_widget(MainWindow())
MainScreenManager.add_widget(SettingsWindow())
MainScreenManager.add_widget(GameWindow())
MainScreenManager.current = "LoadingWindow"

def SetMainScreen(dt) :
	MainScreenManager.current = "MainWindow"

Clock.schedule_once(SetMainScreen, 5)

class GameApp(App) :
	def build(self) :
		return(MainScreenManager)

if(__name__ == "__main__") :
	GameApp().run()