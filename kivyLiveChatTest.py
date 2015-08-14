from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import requests
from firebase import firebase



inputText = ""

class testLiveChatApp(App):
	def build(self):
		root = self.setupUI()
		return root


	def inputTextChanged(instance,value):
		self.inputText = value.text
		print(self.inputText)



	def enterChat(instance, value):
		print(value.text)

	def setupUI(self):
		layout = BoxLayout(orientation = 'vertical')
		inputLayout = BoxLayout(orientation = 'horizontal', size_hint_y=(.05))
		sendButton = Button(text = 'Enter', size_hint_x = (.2))
		sendButton.bind(on_press=self.enterChat)
		textInput = TextInput(text = 'Please enter your message!', multiline = False)
		textInput.bind(text=self.inputTextChanged)
	

		
		inputLayout.add_widget(textInput)
		inputLayout.add_widget(sendButton)

		title = Label(text = "Welcome to X's experimental live chat App!")
		layout.add_widget(title)
		layout.add_widget(inputLayout)

		return layout


	




if __name__ == '__main__':
	testLiveChatApp().run()