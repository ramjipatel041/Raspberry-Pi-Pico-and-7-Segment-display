from machine import Pin
import utime

a = Pin(0, Pin.OUT)
b = Pin(1, Pin.OUT)
c = Pin(2, Pin.OUT)
d = Pin(3, Pin.OUT)
e = Pin(4, Pin.OUT)
f = Pin(5, Pin.OUT)
g = Pin(6, Pin.OUT)

C0 = Pin(7, Pin.OUT)
C1 = Pin(8, Pin.OUT)

number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display(num):
    for i in num:
        if i == "0":
            a.value(1)
            b.value(1)
            c.value(1)
            d.value(1)
            e.value(1)
            f.value(1)
            g.value(0)
        elif i == "1":
            a.value(0)
            b.value(1)
            c.value(1)
            d.value(0)
            e.value(0)
            f.value(0)
            g.value(0)
        elif i == "2":
            a.value(1)
            b.value(1)
            c.value(0)
            d.value(1)
            e.value(1)
            f.value(0)
            g.value(1)
        elif i == "3":
            a.value(1)
            b.value(1)
            c.value(1)
            d.value(1)
            e.value(0)
            f.value(0)
            g.value(1)
        elif i == "4":
            a.value(0)
            b.value(1)
            c.value(1)
            d.value(0)
            e.value(0)
            f.value(1)
            g.value(1)
        elif i == "5":
            a.value(1)
            b.value(0)
            c.value(1)
            d.value(1)
            e.value(0)
            f.value(1)
            g.value(1)
        elif i == "6":
            a.value(1)
            b.value(0)
            c.value(1)
            d.value(1)
            e.value(1)
            f.value(1)
            g.value(1)
        elif i == "7":
            a.value(1)
            b.value(1)
            c.value(1)
            d.value(0)
            e.value(0)
            f.value(0)
            g.value(0)
        elif i == "8":
            a.value(1)
            b.value(1)
            c.value(1)
            d.value(1)
            e.value(1)
            f.value(1)
            g.value(1)
        elif i == "9":
            a.value(1)
            b.value(1)
            c.value(1)
            d.value(1)
            e.value(0)
            f.value(1)
            g.value(1)
while True:
    for i in range(10):
        display(str(i))
        utime.sleep(0.2)
    
    
   
    
    
    
            


            

            


            
