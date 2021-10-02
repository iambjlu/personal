import RPi.GPIO as GPIO
import tkinter as tk
  
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
  
pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(0)
 
root=tk.Tk()
root.title("LED PWM Controller")
root.geometry('300x100')
 
counter=0
var=tk.StringVar()
var.set(str(counter))
label=tk.Label(root,textvariable=var,font=('Piboto',14),bg='#8aa294',fg='#22391F',width=30,height=2)
label.pack()
 
def add1():
    global counter
    if counter>=100:
        counter=100
    else:
        counter = counter +1
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)
     
def sub1():
    global counter
    if counter<=0:
        counter=0
    else:
        counter = counter -1
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)
     
def clear():
    global counter
    counter=0
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)

def setentry():
    global counter
    counter=(brightness.get())
    var.set(str(counter))
    pwm_led.ChangeDutyCycle(counter)
 
brightness=tk.Entry(root,font=('Piboto',12))
bset=tk.Button(root,text="-1",font=('Piboto',12),bg='#8aa294',fg='#22391F',width=8,height=1,command=setentry)
btn1=tk.Button(root,text="-1",font=('Piboto',12),bg='#8aa294',fg='#22391F',width=8,height=1,command=sub1)
btn2=tk.Button(root,text="+1",font=('Piboto',12),bg='#8aa294',fg='#22391F',width=8,height=1,command=add1)
btn3=tk.Button(root,text="Clear",font=('Piboto',12),bg='#8aa294',fg='#22391F',width=8,height=1,command=clear)
 
btn1.pack(side=tk.LEFT)

btn2.pack(side=tk.RIGHT)
btn3.pack(side=tk.LEFT)
brightness.pack(side=tk.RIGHT)
 
root.mainloop()
