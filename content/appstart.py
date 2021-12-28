#КАК Я МОГУ ВЗАИМОДЕЙСТВОВАТЬ С ИНФОРМАЦИЕЙ ВВЕДЕННОЙ В LABEL KIVY PYTHON
#КАК МНЕ ОБМЕНИВАТЬСЯ ФУНКЦИЯМИ МЕЖДУ ДВУМЯ ФАЙЛАМИ PYTHOM
#СДЕЛАТЬ LOVER() Keeglx
#сделать браузер на пайтоне!!!


import os

import time 
from kivy.app import App

from kivy.uix.button import Button 

from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.anchorlayout import AnchorLayout 

from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 

from choice import Choice 

from kivy.uix.widget import Widget 


from image2 import Image2 


import webbrowser

from playsound import playsound
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class For_Friends(App):


	def __init__(self, **kwargs):
		super (For_Friends, self).__init__(**kwargs)

		self.wd = Widget()

		self.text_input = TextInput(
							text = '',
							multiline = False,
							size_hint = (None, None),
							size = (200, 30))


		self.btn_yes = Button(
						text = 'yes',
						font_size = 20,
						size_hint = (None, None),
						size = (150, 70),
						background_normal = '',
						background_color = [1, 0, 0, 1],
						on_press = self.next_leve1)

		self.btn_no = Button(
						text = 'no',
						font_size = 20,
						size_hint = (None, None),
						size = (150, 70),
						background_normal = '',
						background_color = [1, 0, 0, 1],
						on_press =  self.presed_no)

		self.btn_check = Button(
							text = 'check',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.checking)

		self.btn_next_level = Button(
							text = 'next level',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.level_2)

		self.btn_name = Button(
							text = 'this is my name',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.check_name)

		self.btn_thank = Button(
							text = 'thanks) next level',
							font_size = 20,
							size_hint = (None, None),
							size = (170, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.main_level_2)


		self.btn_img2 = Button(
							text = 'image_2',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.img2_presed)

		self.input_img2 = TextInput(
							text = '',
							hint_text = 'изображение 2',
							multiline = False,
							size_hint = (None, None),
							size = (200, 30))

		self.btn_check_img2 = Button(
							text = 'check',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.check_img2)



		self.btn_next_level3 = Button(
							text = 'next level',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.go_cite)

		self.btn_go_cite = Button(
							text = 'NOT PRESS!!!',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.go_cite)

		

	def bald(self):
		self.bl = BoxLayout(padding = 10, orientation = 'vertical')
		self.gl = GridLayout(cols = 2, spacing = 20, size_hint = (.4, .5)) 
		self.al = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
		self.al_button = AnchorLayout(anchor_x = 'center', anchor_y = 'center')

		self.bt_start = Button(
					text = 'start',
					font_size = 20,
					size_hint = (None, None),
					size = (150, 70),
		 			background_normal = '',
					background_color = [1, 0, 0, 1],
					on_press = self.chs)

		self.al.add_widget(self.bt_start)
		self.bl.add_widget(self.al, len(self.bl.children))


		return self.bl
	def chs(self, instance):
		self.al.remove_widget(self.bt_start)
		
		self.txt_hello = Label(text = 'Привет, хочешь поиграть со мной?')

		self.al.add_widget(self.txt_hello)	

		
		
		self.gl.add_widget(self.btn_yes)
		self.gl.add_widget(self.btn_no)
		self.al_button.add_widget(self.gl)
		self.bl.add_widget(self.al_button)
		
		Choice.main()

	def presed_no(self, instance):
		self.gl.remove_widget(self.btn_no)
		self.txt_hello.txt = 'неугадали!'


	#LEVEL I 
	def next_leve1(self, instance):
		self.gl.remove_widget(self.btn_yes)
		self.gl.remove_widget(self.btn_no)
		self.bl.remove_widget(self.al_button)	

			

		self.gl.size_hint = (1, 1)
		self.gl.cols = 1
		

		self.al_button.remove_widget(self.gl)
		self.txt_hello.text = '''хороший выбор! \n давай поиграем в игру "угадай слово"\nтебе нужно найти файл, который я только что создал,\nи вписать ниже слово, которое на написано'''
		

		self.text_input.hint_text = 'введите слово сдесь'
		self.gl.add_widget(self.text_input)
		

		self.gl.add_widget(self.btn_check)
		self.bl.add_widget(self.gl)

		self.creating_file()

		#OS
	def creating_file(self):
		text = open('missed_me.txt', 'w')
		a = 'сдохни'
		text.write(a)

	def checking(self, instance):
		words_1 = str(self.text_input.text)
		if words_1 == 'сдохни' or words_1 == 'q':
			self.txt_hello.text = 'вы ввели верное слово!'
			self.gl.remove_widget(self.text_input)
			self.gl.add_widget(self.btn_next_level)
			self.gl.remove_widget(self.btn_check)
			self.text_input.text = ''


		else:
			self.txt_hello.text = "введеное вами слово не правильное!"
			self.text_input.text = ''

	def level_2(self, instance):

		self.gl.add_widget(self.text_input)
		self.text_input.text = ''
		self.text_input.hint_text = 'Введите имя на русском'
		self.gl.remove_widget(self.btn_check)
		self.gl.remove_widget(self.btn_next_level)

		self.txt_hello.text = 'совсем забыл спросить, как тебя зовут?'
		self.gl.add_widget(self.btn_name)
		

	def check_name(self, instance):
		name = str(self.text_input.text.lower())
		if name == 'лера' or name == 'валерия' or name == 'lera':
			self.here_is_lera()

		else:
			self.not_is_lera()

	def here_is_lera(self):
		self.gl.remove_widget(self.btn_name)
		self.text_input.text = ''
		self.gl.remove_widget(self.text_input)
		self.txt_hello.text = '''Ты действительно играешь в мою игру?\nЯ не могу поверить\nпросто эту игру написал Нимай и он очень обрадуется,\nПотому что ТЫ играешь именно в эту игру\nНаслаждайтесь игрой =)\n P.s. скажу тебе по серкрету, ты ему нравишься\n но это между нами'''
		self.gl.add_widget(self.btn_thank)

	def not_is_lera(self):
		self.gl.remove_widget(self.btn_name)
		self.text_input.text = ''
		self.gl.remove_widget(self.text_input)
		self.txt_hello.text = 'ну что, следующий уровень?'
		self.gl.add_widget(self.btn_thank)

	def main_level_2(self, instance):
		self.gl.remove_widget(self.btn_thank)
		self.gl.remove_widget(self.text_input)
		self.gl.cols = 3
		
		self.txt_hello.text = 'ниже есть кнопочка, и если на них нажать, то вылезет картинка \n твоя задача подписать что это за картинка)))'

		self.gl.add_widget(self.btn_img2)
		self.gl.add_widget(self.input_img2)
		self.gl.add_widget(self.btn_check_img2)	


	def check_img2(self, instance):
		
		ansvel = str(self.input_img2.text.lower())
		if ansvel == 'котик' or ansvel == 'cat':
			self.txt_hello.text = 'Вот бы себе такого)'
			
			self.gl.remove_widget(self.btn_check_img2)
			self.gl.remove_widget(self.btn_img2)
			self.gl.remove_widget(self.input_img2)

			self.gl.add_widget(self.btn_go_cite)	
			
			

		else:
			self.txt_hello.text = 'не-а, что то не так ввели \n попробуйте по другому'

		


	def img2_presed(self, instance):
		#нормальная картинка
		Image2.go_image2()	
		

	def go_cite(self, instance):
		self.gl.remove_widget(self.btn_go_cite)
		webbrowser.open('source/cite.html')
		self.btn_go_cite.on_press = self.level_4


	def level_4(self):
		self.txt_hello.text = 'как сайт?'


	def build(self):
		return self.bald()

