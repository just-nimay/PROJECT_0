from appstart import For_Friends

from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'haight', 500)


if __name__ == '__main__':
    For_Friends().run()  