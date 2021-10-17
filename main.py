from kivy.app import App
from kivy.uix.label import Label

class GameApp(App):
	def build(self):
		return Label(text='HELLO WORLD', font_size=70)
		
if __name__ == '__main__':
	GameApp().run()