from kivy.app import App 

from playsound import playsound
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Image2(App):
	def go_image2():
		#нормальная картинка
		play = playsound
		img = plt.imshow(mpimg.imread('music/img/cat.jpg'))
		#показ картинки
		plt.show()
		#ожидание 3 секунды
		time.sleep(3)
		#показ скримера
		img_2 = plt.imshow(mpimg.imread('music/img/scrimer_1.jpg'))
		plt.ion()
		plt.show()
		#воспроизведение скримера
		playsound('music/sound_1.WAV')
		
		
