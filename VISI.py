from machine import Pin, PWM
from utime import sleep
import RGB1602
colorR = 64
colorG = 128
colorB = 64

lcd = RGB1602.RGB1602(16,2)

r_lcd = (255,20,0)
o_lcd = (255,80,10)
g_lcd = (20,160,10)
k_lcd = (0,0,0)

R_LED = PWM(Pin(9))
R_LED.freq(1000)
G_LED = PWM(Pin(10))
G_LED.freq(1000)
B_LED = PWM(Pin(11))
B_LED.freq(1000)

r_button = Pin(16,Pin.IN,Pin.PULL_DOWN)
o_button = Pin(17,Pin.IN,Pin.PULL_DOWN)
g_button = Pin(19,Pin.IN,Pin.PULL_DOWN)
k_button = Pin(22,Pin.IN,Pin.PULL_DOWN)

while True:
    if r_button.value():
        
        R_LED.duty_u16(65535)
        G_LED.duty_u16(0)
        B_LED.duty_u16(0)
                
        lcd.setRGB(r_lcd[0],r_lcd[1],r_lcd[2]);
        lcd.clear()
        sleep(0.25)        
        lcd.setCursor(0, 0)
        lcd.printout("On a call, can't")
        lcd.setCursor(0, 1)
        lcd.printout("talk right now.")
        
        sleep(0.5)

    if o_button.value():
        
        R_LED.duty_u16(60000)
        G_LED.duty_u16(10000)
        B_LED.duty_u16(0)
        
        lcd.setRGB(o_lcd[0],o_lcd[1],o_lcd[2]);
        lcd.clear()
        sleep(0.25)        
        lcd.setCursor(0, 0)
        lcd.printout("On a call, but")
        lcd.setCursor(0, 1)
        lcd.printout("free to chat.")
        
        sleep(0.5)

    if g_button.value(): 
                
        G_LED.duty_u16(30000)
        B_LED.duty_u16(100)
        R_LED.duty_u16(0)
                       
        lcd.setRGB(g_lcd[0],g_lcd[1],g_lcd[2]);
        lcd.clear()
        sleep(0.25)
        lcd.setCursor(0, 0)
        lcd.printout("Just listening.")
        lcd.setCursor(0, 1)
        lcd.printout("Free to chat.")
        
        sleep(0.5)
        
    if k_button.value(): 
              
        G_LED.duty_u16(0)
        B_LED.duty_u16(0)
        R_LED.duty_u16(0)
        
        lcd.setRGB(k_lcd[0],k_lcd[1],k_lcd[2]);
        lcd.clear()       

        sleep(0.5)        