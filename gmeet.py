#importing required modules
from time import sleep
import webbrowser
import pyautogui as py

#to get link
link = input("Paste the link: ")

#joining functions
def join():
    joinX,joinY = 988,545     #change this
    iconX,iconY = 1222,160    #change this
    boxX,boxY = 994,724       #change this
    sendX,sendY = 1318,729    #change this

    #opening in browser
    webbrowser.open_new(link)
    sleep(30)                 #change this
    py.click(joinX,joinY)
    sleep(5)                  #change this
    py.click(iconX,iconY)
    sleep(3)                  
    py.click(boxX,boxY)
    sleep(1)
    py.write("Hello Good Morning", interval = 0.25)
    sleep(1)
    py.click(sendX,sendY)

join()
