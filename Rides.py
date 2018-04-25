import time 
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import thread
import urllib2

command = [0,0]
destination = ["ITESO","ITESO"]

def LCD_print(LCD):
	while 1:
            lcd1.clear()
            lcd1.message(destination[0])
            lcd2.clear()
            lcd2.message(destination[1])

def JSON(status):
	link = "http://paginalocal.net:3000/button-info"
	i = 0
	while 1:
	    j = urllib2.urlopen(link)
            myjson = j.read()
            destination[0],command[0],destination[1],command[1], aux1, aux2, aux3 = myjson.split("\n")
            time.sleep(2)

#def button_pressed(channel):



#Pins for LCD1
lcd1_rs		= 25
lcd1_en		= 24
lcd1_d4		= 23
lcd1_d5		= 17
lcd1_d6		= 18
lcd1_d7		= 22
lcd1_backlight	= 2

lcd_columns 	= 16
lcd_rows	= 2

#Init first LCD
lcd1 = LCD.Adafruit_CharLCD(lcd1_rs, lcd1_en, lcd1_d4, lcd1_d5, lcd1_d6, lcd1_d7, lcd_columns, lcd_rows, lcd1_backlight)

#Pins for LCD1
lcd2_rs		= 6
lcd2_en		= 12
lcd2_d4		= 19
lcd2_d5		= 16
lcd2_d6		= 20
lcd2_d7		= 26
lcd2_backlight	= 2

#Init first LCD
lcd2 = LCD.Adafruit_CharLCD(lcd2_rs, lcd2_en, lcd2_d4, lcd2_d5, lcd2_d6, lcd2_d7, lcd_columns, lcd_rows, lcd2_backlight)

thread.start_new_thread(LCD_print, ('1',))

thread.start_new_thread(JSON, (1,))

while 1:
	pass
