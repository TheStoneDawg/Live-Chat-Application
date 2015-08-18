from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import requests
from firebase import firebase

from kivy.uix.listview import ListView
from kivy.adapters.simplelistadapter import SimpleListAdapter





class testLiveChatApp(App):
	data = ["Welcome to X's experimental live chat App!"]
	inputText = "Please enter your message!"
	def build(self):
		self.getData(self,0)
		root = self.setupUI()
		return root


	def inputTextChanged(self,instance,value):
		self.inputText = value


	def getData(self,instance,value):
		SamChungsFirebase = firebase.FirebaseApplication('https://kivytestlivechat.firebaseio.com/',None)
		data = SamChungsFirebase.get('/', None)
		for key in data:
			message = data[key]
			self.data.append(message)






	def enterChat(self,instance):
		SamChungsFirebase = firebase.FirebaseApplication('https://kivytestlivechat.firebaseio.com/',None)
		message = self.inputText
		SamChungsFirebase.post('/', message)
		self.getData(self,instance)
		self.root = self.setupUI()

	def setupUI(self):
		layout = BoxLayout(orientation = 'vertical')
		inputLayout = BoxLayout(orientation = 'horizontal', size_hint_y=(.05))
		sendButton = Button(text = 'Enter', size_hint_x = (.2))
		sendButton.bind(on_press=self.enterChat)
		textInput = TextInput(text = 'Please enter your message!', multiline = False)
		textInput.bind(text=self.inputTextChanged)
	

		
		inputLayout.add_widget(textInput)
		inputLayout.add_widget(sendButton)
		chatListView = ListView(item_strings=self.data)
		layout.add_widget(chatListView)
		layout.add_widget(inputLayout)

		return layout


	def updateUI(self):
		self.root.clear_widgets()

		layout = BoxLayout(orientation = 'vertical')
		inputLayout = BoxLayout(orientation = 'horizontal', size_hint_y=(.05))
		sendButton = Button(text = 'Enter', size_hint_x = (.2))
		sendButton.bind(on_press=self.enterChat)
		textInput = TextInput(text = 'Please enter your message!', multiline = False)
		textInput.bind(text=self.inputTextChanged)
	

		
		inputLayout.add_widget(textInput)
		inputLayout.add_widget(sendButton)
		chatListView = ListView(item_strings=self.data)
		layout.add_widget(chatListView)
		layout.add_widget(inputLayout)

		return layout




if __name__ == '__main__':
	testLiveChatApp().run()