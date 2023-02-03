from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.boxlayout import BoxLayout

from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
import pickle
import mysql.connector


#login form
import tkinter as tk



# connect with mysql database
connection = mysql.connector.connect(
     host='localhost',
     user='root',
     password='#Abhishek786',
     port='3306',
     database='login_base'
)

c = connection.cursor()
select_query='SELECT * FROM `login`'

c.execute(select_query)
print(c.fetchall())
root = tk.Tk()


class ProfileCreate(App):

    def build(self):
        screen = Builder.load_string(ScreenManager)
        return screen


class SignUpScreen(Screen):
    signuperror = StringProperty()

    def signup(self):
        sigingupusername = self.ids.signupusername.text
        siginguppassword = self.ids.signuppassword.text

        if (sigingupusername == '' and siginguppassword == ''):
            print('Text cant be empty')
            self.signuperror = str('Text Cant be empty')




        else:
            sigingupusername = pickle.dump(sigingupusername, open("Signupusername", "wb"))
            siginguppassword = pickle.dump(siginguppassword, open("Signuppassword", "wb"))

            sigingupusername = self.ids.signupusername.text = ''
            siginguppassword = self.ids.signuppassword.text = ''
            self.parent.current = 'Profile'
            self.signuperror = str()


class LoginScreen(Screen):
    loginerror = StringProperty()

    def login(self):
        createdusername = self.ids.loginusername.text
        createdpassword = self.ids.loginpassword.text
        signingupusername = pickle.load(open("Signupusername", "rb"))
        signinguppassword = pickle.load(open("Signuppassword", "rb"))

        if signingupusername == createdusername and signinguppassword == createdpassword:
            print('correct username and password')
            self.loginerror = str()

            self.parent.current = 'Profile'
        elif signingupusername != createdusername and signinguppassword != createdpassword:
            print('incorrect username and password')
            self.loginerror = str('Incorrect Username/Password')

        elif signingupusername == createdusername and signinguppassword != createdpassword:
            print('incorrect username and password')
            self.loginerror = str('Incorrect Username/Password')

        elif signingupusername != createdusername and signinguppassword == createdpassword:
            print('incorrect username and password')
            self.loginerror = str('Incorrect Username/Password')


class ProfileScreen(Screen):
    pass
class Mainscreen(Screen):
	pass
class Fscreenone(Screen):
	pass
class sportscreen(Screen):
	pass
class mscreen(Screen):
	pass
class sportscreentwo(Screen):
	pass
class mscreentwo(Screen):
	pass
kv=Builder.load_file('TheLab.kv')
class LoginApp(App):
    def build(self):
        return kv
# sm = ScreenManager()
# sm.add_widget(LoginScreen(name='Login'))
# sm.add_widget(SignUpScreen(name='Sign'))
# sm.add_widget(ProfileScreen(name='Profile'))

LoginApp().run()
