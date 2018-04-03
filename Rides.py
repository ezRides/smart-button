#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

global flag

def button_pressed(channel):
    lcd.clear()
    lcd.message('IP:')
    file.seek(0, 0)
    ip = file.readline()
    lcd.message(ip)
    time.sleep(5.0)
    print("Im in callback")


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(14, GPIO.FALLING, callback=button_pressed, bouncetime=500)

flag = 0
lcd_rs        = 25 
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 2
lcd_columns = 16
lcd_rows = 2
file = open('Message.txt', 'r')

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
ip = file.readline()

while(1):
    if GPIO.input(14) == 0:
        lcd.clear()
        file.seek(0, 0)
        file.readline()
        message = file.readline()
        lcd.message(message)
        time.sleep(2.0)
    else:
        lcd.clear()
        lcd.message('Hola')
        time.sleep(2.0)
        

#except KeyboardInterrupt:  
#    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  



