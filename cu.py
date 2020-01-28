from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set up
chromeDriver = '.\\chromeDrivers\\chromeDriver'
chromeDriver18 = '.\\chromeDrivers\\chromeDriver18'
chromeDriver19 = '.\\chromeDrivers\\chromeDriver19'

us = input('username: ')
ps = input('password: ')


# code
class CuBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        try:
            self.bot = webdriver.Chrome(chromeDriver)
        except:
            try:
                self.bot = webdriver.Chrome(chromeDriver19)
            except:
                self.bot = webdriver.Chrome(chromeDriver18)

    def login(self):
        bot = self.bot
        bot.get('https:programs.cu.edu.ge/cu/loginStud')
        nick = bot.find_element_by_name('username')
        passwd = bot.find_element_by_name('password')
        nick.send_keys(self.username)
        passwd.send_keys(self.password)
        passwd.send_keys(Keys.RETURN)

    def marks(self):
        bot = self.bot
        bot.get('https://programs.cu.edu.ge/students/gpa.php')


ir = CuBot(us, ps)
ir.login()
ir.marks()
