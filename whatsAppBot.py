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
        
        
    def nav_green_dot(self):
        try:
            position = pt.locateAllOnScreen('NewMessageSign.png', confidence=.8)
            position = list(position)
            pt.moveTo(position[0].left, position[0].top, duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Exception(nav_green_dot): " ,e)
            
            
wa_bot = WhatsApp(speed=.5, click_speed=.4)
wa_bot.nav_green_dot()