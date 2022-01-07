import os
import subprocess
# получение текущей дириктории
directory = os.getcwd()
# добавление в текущей дирктории /content
dir_con = (directory + '/content')

# запуск установки pip
subprocess.call('python3 ' + str(dir_con) + '/get-pip.py', shell=True)

subprocess.call('python3 pip -m install kivy[base]', shell=True)

subprocess.call('pip3 install playsound', shell=True)

subprocess.call('pip3 install matplotlib', shell=True)

subprocess.call('python3 ' + str(dir_con) + '/appstart.py', shell=True)