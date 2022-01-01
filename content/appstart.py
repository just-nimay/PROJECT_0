#|== RUSSIAN =========================================================|
#|Всем Привет! Меня зовут Нимай, и я начинающий разработчик.          |
#|Это моя первая "типо игра", поэтому прошу отнестить с пониманием    |
#|--------------------------------------------------------------------|
#|Со мной можно связатся с помощью:                                   |
#|Дискорд: #7295                                                      |
#|Тереграм: @Just_Nimay                                               |
#|почта: just_nimay@vk.com                                            |
#|                                                                    |
#|== ENGLISH =========================================================|

import os

import time 
from kivy.app import App

from kivy.uix.button import Button 

from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.anchorlayout import AnchorLayout 

from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 

# Это для того, что бы скример выскакивал
from image2 import Image2 


import webbrowser

from playsound import playsound
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#неизменяемое окна
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'haight', 500)



class For_Friends(App):

	#сдесь хронятся все кнопки, поля для ввода, выводящиеся поля с текстами
	def __init__(self, **kwargs):
		super (For_Friends, self).__init__(**kwargs)


		self.text_input = TextInput(
							text = '',
							multiline = False,
							size_hint = (None, None),
							size = (200, 30))

		# кнопка 'yes'
		self.btn_yes = Button(
						text = 'yes',
						font_size = 20,
						size_hint = (None, None),
						size = (150, 70),
						background_normal = '',
						background_color = [1, 0, 0, 1],
						on_press = self.next_leve1)

		# кнопка 'no'
		self.btn_no = Button(
						text = 'no',
						font_size = 20,
						size_hint = (None, None),
						size = (150, 70),
						background_normal = '',
						background_color = [1, 0, 0, 1],
						on_press =  self.presed_no)

		# кнопка проверки
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

		#  кнопка, которая выводит изображение 
		self.btn_img2 = Button(
							text = 'image_2',
							font_size = 20,
							size_hint = (None, None),
							size = (150, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.img2_presed)

		#инпут для ввода того, что находится на изображении
		self.input_img2 = TextInput(
							text = '',
							hint_text = 'изображение 2',
							multiline = False,
							size_hint = (None, None),
							size = (200, 30))

		#проверяет что введено в инпут для ввода того, что находится на изображении
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


		self.btn_otziv = Button(
							text = 'отправить отзыв',
							font_size=20,
							size_hint = (None, None),
							size = (180, 70),
							background_normal = '',
							background_color = [1, 0, 0, 1],
							on_press = self.otziv)

		

	def bald(self):
		#этот лояут берет в себя все остальные(основа)
		self.bl = BoxLayout(padding = 10, orientation = 'vertical')
		#в этот лаяут помещаются кнопки, инпуты, и иногда тексты
		self.gl = GridLayout(cols = 2, spacing = 20, size_hint = (.4, .5)) 
		# этот лаяут содержит текст, который видет пользователю
		self.al = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
		# для нескольких кнопок на одном уровне, что бы смотрелось красиво 
		self.al_button = AnchorLayout(anchor_x = 'center', anchor_y = 'center')

		# кнопка начала
		self.bt_start = Button(
					text = 'start',
					font_size = 20,
					size_hint = (None, None),
					size = (150, 70),
		 			background_normal = '',
					background_color = [1, 0, 0, 1],
					on_press = self.chs)

		#добавляет кнопку start
		self.al.add_widget(self.bt_start)
		self.bl.add_widget(self.al, len(self.bl.children))

		#показывает все что есть в boxlayout
		return self.bl
	def chs(self, instance):
		playsound('music/blip2.wav')
		#убирает кнопку start
		self.al.remove_widget(self.bt_start)
		
		# присваивание текста к выводу текста
		self.txt_hello = Label(text = 'Привет, хочешь поиграть со мной?')
		#добавление self.txt_hello в anchorlayout
		self.al.add_widget(self.txt_hello)	

		
		#добавление кнопки yes в greedlayout
		self.gl.add_widget(self.btn_yes)

		#добавление кнопки no в greedlayout
		self.gl.add_widget(self.btn_no)

		#добавление greedlayot в al_button 
		self.al_button.add_widget(self.gl)

		#добавление al_button в boxlayout
		self.bl.add_widget(self.al_button)
		
		
	# если пользователь нажал no
	def presed_no(self, instance):
		playsound('music/shoot.WAV')
		#удаление кнопки no
		self.gl.remove_widget(self.btn_no)
		self.txt_hello.txt = 'неугадали!'

	# если пользователь нажал yes
	#LEVEL I 
	def next_leve1(self, instance):
		playsound('music/blip2.wav')
		#удаление ненужных кнопок
		self.gl.remove_widget(self.btn_yes)
		self.gl.remove_widget(self.btn_no)
		self.bl.remove_widget(self.al_button)	

			
		#создание колон в greedlayout'е
		self.gl.size_hint = (1, 1)
		self.gl.cols = 1
		
		#удаление greedlayout'a их al_bitton'a
		self.al_button.remove_widget(self.gl)
		self.txt_hello.text = '''хороший выбор! \nдавай поиграем в игру "угадай слово"\nтебе нужно найти файл, который я только что создал,\nи вписать ниже слово, которое на написано'''
		
		#присвоение инпуту текста-подсказки
		self.text_input.hint_text = 'введите слово сдесь'
		#добавление инпута в greedlayout
		self.gl.add_widget(self.text_input)
		
        # добавление кнопки проверки инпута №1 в greedlayout
		self.gl.add_widget(self.btn_check)
		self.bl.add_widget(self.gl)

		# вызов функции, которая создает файл
		self.creating_file()

		#функция, создающая файл
	def creating_file(self):
		#создание файла
		directory = 'just_folder/im_for_you.txt'
		folder_path = os.path.dirname(directory)
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)

		with open(directory, 'w') as file:
			file.write('сдохни')
		#текс, который будет записан в файл


	#проверка инпута №1 
	def checking(self, instance):
		playsound('music/Paste.wav')
		#присваивание переменной words_1 текста, который находится в text_input
		words_1 = str(self.text_input.text)

		if words_1 == 'сдохни' or words_1 == 'q':
			self.txt_hello.text = 'вы ввели верное слово!'

			#удаление кнопки проверки
			self.gl.remove_widget(self.btn_check)
			self.gl.remove_widget(self.text_input)
			#добавление кнопки next_level
			self.gl.add_widget(self.btn_next_level)
			#очищение поля текста, видимого для пользователя
			self.text_input.text = ''


		else:
			self.txt_hello.text = "введеное вами слово не правильное!"
			#очищение поля для ввода
			self.text_input.text = ''

	# LEVEL_2
	def level_2(self, instance):
		playsound('music/blip2.wav')
		self.gl.add_widget(self.text_input)
		self.text_input.text = ''
		#присваивание input'у нового текста подсказки
		self.text_input.hint_text = 'Введите имя на русском'
		self.gl.remove_widget(self.btn_check)
		self.gl.remove_widget(self.btn_next_level)

		self.txt_hello.text = 'совсем забыл спросить, как тебя зовут?'
		self.gl.add_widget(self.btn_name)
		

	def check_name(self, instance):
		#присваивание переменной name текста, который находится в text_input
		#lover() - переводит текст в input'e в нижний регистр
		name = str(self.text_input.text.lower())
		if name == 'лера' or name == 'валерия' or name == 'lera':
			self.here_is_lera()

		elif name =='':
			self.txt_hello.text = 'ну нет, так не пойдет. \n вводи свое имя'
		else:
			self.not_is_lera()

	def here_is_lera(self):
		playsound('music/blip2.wav')
		self.gl.remove_widget(self.btn_name)
		self.text_input.text = ''
		self.gl.remove_widget(self.text_input)
		self.txt_hello.text = '''Ты действительно играешь в мою игру?\nЯ не могу поверить\nпросто эту игру написал Нимай и он очень обрадуется,\nПотому что ТЫ играешь именно в эту игру\nНаслаждайтесь игрой =)\n P.s. скажу тебе по серкрету, ты ему нравишься\n но это между нами'''
		self.gl.add_widget(self.btn_thank)

	def not_is_lera(self):
		playsound('music/Paste.wav')
		self.gl.remove_widget(self.btn_name)
		self.text_input.text = ''
		self.gl.remove_widget(self.text_input)
		self.txt_hello.text = 'ну что, следующий уровень?'
		self.gl.add_widget(self.btn_thank)

	def main_level_2(self, instance):
		playsound('music/blip2.wav')
		self.gl.remove_widget(self.btn_thank)
		self.gl.remove_widget(self.text_input)
		#создание трех колон, для трех элементов
		self.gl.cols = 3
		self.txt_hello.txt=''
		self.txt_hello.text = 'ниже есть кнопочка, и если на них нажать, то вылезет картинка \n твоя задача подписать что это за картинка)))'

		self.gl.add_widget(self.btn_img2)
		self.gl.add_widget(self.input_img2)
		self.gl.add_widget(self.btn_check_img2)	


	def check_img2(self, instance):
		playsound('music/Paste.wav')
		#присваивание переменной ansvel текста, который находится в text_input
		ansvel = str(self.input_img2.text.lower())
		if ansvel == 'котик' or ansvel == 'cat':
			self.txt_hello.text = 'Вот бы себе такого)'
			#удаление ненужных элементов
			self.gl.remove_widget(self.btn_check_img2)
			self.gl.remove_widget(self.btn_img2)
			self.gl.remove_widget(self.input_img2)
			#добавление кнопки ведущей на сайт
			self.gl.add_widget(self.btn_go_cite)	
			
			

		else:
			self.txt_hello.text = 'не-а, что то не так ввели \n попробуйте по другому'

		

	#скример
	def img2_presed(self, instance):
		playsound('music/shoot.WAV')

		#нормальная картинка
		play = playsound
		img = plt.imshow(mpimg.imread('music/img/cat.jpg'))
		#показ картинки
		plt.show()
		#ожидание 3 секунды
		time.sleep(1.5)
		
		img_2 = plt.imshow(mpimg.imread('music/img/scrimer_1.jpg'))
		#воспроизведение скримера
		
		playsound('music/sound_1.WAV', False)

		#показ скримера
		plt.show()
		
		

	#перевод на сайт
	def go_cite(self, instance):
		new = 2 # open in a new tab, if possible
		playsound('music/shoot.WAV')
		self.gl.remove_widget(self.btn_go_cite)
		directory = os.getcwd()
		url = 'file://{}/site.html'.format(directory)
		print('url: ' + url, directory)
		webbrowser.open(url)
		self.btn_go_cite.on_press = self.level_4

	def level_4(self):
		self.txt_hello.text = 'как сайт?'
		#добавление элементов
		self.gl.add_widget(self.text_input)
		self.gl.add_widget(self.btn_otziv)
		self.text_input.hint_text = 'Отзыв'
		


	def otziv(self, instance):
		playsound('music/blip2.wav')
		if self.text_input.text == 'ужасно хорошо':
			self.txt_hello.text = 'В таком случае могу вас порадовать, разраб этой игры уже трудится над новой, более реальной игрой))'
			self.gl.remove_widget(self.btn_otziv)
			self.gl.remove_widget(self.text_input)
		else:
			self.txt_hello.text = 'Спасибо за отзыв!'
			self.gl.remove_widget(self.btn_otziv)
			self.gl.remove_widget(self.text_input)

	def build(self):
		#показывает что есть в функции bald
		return self.bald()

if __name__ == '__main__':
    For_Friends().run()  
