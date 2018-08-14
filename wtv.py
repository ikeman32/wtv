 #-*-coding:utf8;-*-
     #qpy:2
     #qpy:kivy
     
import kivy

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.clipboard import Clipboard


phonetic={'a':'alpha','b':'beta','c':'charlie','d':'delta','e':'echo','f':'foxtrot',
'g':'golf','h':'hotel','i':'india','j':'juliet','k':'kilo','l':'lima','m':'mike','n':'november',
'o':'oscar','p':'papa','q':'quebec','r':'romeo','s':'sierra','t':'tango','u':'uniform',
'v':'victor','w':'whiskey','x':'xray','y':'yankey','z':'zulu','\x2E':'delta-oscar-tango',
'\x3A':'charlie-oscar-lima-oscar-november','\x2F':'sierra-lima-alpha-sierra-hotel',
'A':'Alpha','B':'Beta','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot',
'\x20':'sierra-papa-alpha-charlie-echo','\x40':'alpha-tango',
'G':'Golf','H':'Hotel','I':'India','J':'Juliet','K':'Kilo','L':'Lima','M':'Mike','N':'November',
'O':'Oscar','P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform',
'V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankey','Z':'Zulu'}

alpha={'alpha':'a','beta':'b','charlie':'c','delta':'d','echo':'e','foxtrot':'f',
'golf':'g','hotel':'h','india':'i','juliet':'j','kilo':'k','lima':'l','mike':'m','november':'n',
'oscar':'o','papa':'p','quebec':'q','romeo':'r','sierra':'s','tango':'t','uniform':'u',
'victor':'v','whiskey':'w','xray':'x','yankey':'y','zulu':'z','delta-oscar-tango':'\x2E',
'charlie-oscar-lima-oscar-november':'\x3A','sierra-lima-alpha-sierra-hotel':'\x2F','sierra-papa-alpha-charlie-echo':'\x20',
'alpha-tango':'\x40','Alpha':'A','beta':'B','Charlie':'C','Delta':'D','Echo':'E','Foxtrot':'F',
'Golf':'G','Hotel':'H','India':'I','Juliet':'J','Kilo':'K','Lima':'L','Mike':'M','November':'N',
'Oscar':'O','Papa':'P','Quebec':'Q','Romeo':'R','Sierra':'S','Tango':'T','Uniform':'U',
'Victor':'V','Whiskey':'W','Xray':'X','Yankey':'Y','Zulu':'Z'}

class wtv(App):

    def build(self):
        return FloatLayout()

    def clipit(self, text, status):
        address = str(text.text)
        addy = ''
        msg = "Stauts: Your output has been send to the clipboard: \n\n"
        for index in address:
            try:
				addy += phonetic[index] + ' '
            except KeyError:
                pass
        
        Clipboard.copy(addy)
        status.text = msg
        text.text = addy
        
    def pasteit(self, text, status):
	    
        address = str(text.text)
        addy = ''
        msg = "Status: Your output has been send to the clipboard: \n\n"
        for index in address.split():
            try:
				addy += alpha[index]
            except KeyError:
                pass
        
        Clipboard.copy(addy)
        status.text = msg
        text.text = addy
		


if __name__ == '__main__':
    wtv().run()
