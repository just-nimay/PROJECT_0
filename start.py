import os
import subprocess
# получение текущей дириктории
directory = os.getcwd()
# добавление в текущей дирктории /content
dir_con = (directory + '/content')

# запуск установки pip
subprocess.call('python3 ' + str(dir_con) + '/get-pip.py', shell=True)

 # установка библиотеки KIVY
subprocess.call('python3 pip -m install kivy[base]', shell=True)

# установка библиотки playsound
subprocess.call('pip3 install playsound', shell=True)

# установка библиотки matplotlib
subprocess.call('pip3 install matplotlib', shell=True)

# запуск игры
subprocess.call('python3 ' + str(dir_con) + '/appstart.py', shell=True)