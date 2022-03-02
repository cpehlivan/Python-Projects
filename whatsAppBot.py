from multiprocessing.connection import wait
from turtle import pos, position
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

class WhatsApp:
    
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = " "
        self.last_message = " "
        
        
        
    # findet die Position des Bildes und geht darauf zu
    #
    #    
    def nav_green_dot(self):
        try:
            position = pt.locateAllOnScreen('askitompb.png', confidence=.8)
            position = list(position)
            pt.moveTo(position[0].left, position[0].top, duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Exception(nav_green_dot): " ,e)
            
            
    def write_answer(self, text):
        try:
            position = pt.locateAllOnScreen('Bueroklammerzentriert.png', confidence=.8)
            position = list(position)
            pt.moveTo(position[0].left, position[0].top, duration=self.speed)
            pt.moveRel(100,25,duration=self.speed)
            pt.click(interval=self.click_speed)
            pt.write(text)
        except Exception as e:
            print("Exception(bueroklammer): " ,e)
            
            
    def send_answer(self):
        try:
            position = pt.locateAllOnScreen("sendpicture.png", confidence=.9)
            position = list(position)
            pt.moveTo(position[0].left, position[0].top, duration=self.speed) 
            pt.moveRel(25,25)
            pt.click(interval=self.click_speed)  
        except Exception as e:
            print("Exception(sending): " ,e)
            
            
            
wa_bot = WhatsApp(speed=1, click_speed=.4)
wa_bot.nav_green_dot()
wa_bot.write_answer("Seni Seviyorum Askitom!!!")
wa_bot.send_answer()