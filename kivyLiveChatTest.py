from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import requests
from firebase import firebase

from kivy.adapters.listadapter import 





class testLiveChatApp(App):
	inputText = "Please enter your message!"
	def build(self):
		root = self.setupUI()
		return root


	def inputTextChanged(self,instance,value):
		self.inputText = value
		print(self.inputText)


	def getData(self,instance,value):
		SamChungsFirebase = firebase.FirebaseApplication('https://kivytestlivechat.firebaseio.com/',None)
		data = SamChungsFirebase.get('/', None)
		for key in data:
			message = data[key]
			new_Label = Label(text=message)
			self.root.remove_widget()
			self.root.add_widget(new_Label)





	def enterChat(self,instance):
		SamChungsFirebase = firebase.FirebaseApplication('https://kivytestlivechat.firebaseio.com/',None)
		message = self.inputText
		SamChungsFirebase.post('/', message)
		self.getData(self,instance)

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