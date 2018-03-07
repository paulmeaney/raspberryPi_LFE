import RPi.GPIO as GPIO
import time

#LedPin = 11    # pin11

Row1 = 11
Row2 = 13
Col1 = 15
Col2 = 19
Col3 = 21
Col4 = 23

Rows = [11, 13]
Cols = [15, 19, 21,  23]


def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(Rows, GPIO.OUT)
  GPIO.setup(Cols, GPIO.OUT)# Set LedPin's mode is output
  GPIO.output(Cols, GPIO.HIGH)
  GPIO.output(Rows, GPIO.LOW)# Set LedPin high(+3.3V) to turn on led
  print("Running, ctrl+c to end")

def loop():
  while True:    
    
    #allOn()
    allOff()
    lightSelection(11, 13)    
    time.sleep(0.5)
    allOff()
    lightSelection(22)
    time.sleep(0.5)
    allOff()
    lightSelection(21, 23)    
    time.sleep(0.5)
    allOff()
    lightSelection(12)    
    time.sleep(0.5)
    

def destroy():
    GPIO.output(Cols, GPIO.LOW)
    GPIO.output(Rows, GPIO.LOW)   # led off
    GPIO.cleanup()

def allOff():
    GPIO.output(Cols, GPIO.HIGH)
    GPIO.output(Rows, GPIO.LOW)

def allOn() :
    GPIO.output(Cols, GPIO.LOW)
    GPIO.output(Rows, GPIO.HIGH)
    
def lightSelection(*lights):
    for light in lights:
        if light == 11:
           GPIO.output(Row1, GPIO.HIGH)
           GPIO.output(Col1, GPIO.LOW)
        elif light == 12:
           GPIO.output(Row1, GPIO.HIGH)
           GPIO.output(Col2, GPIO.LOW)
        elif light == 13:
           GPIO.output(Row1, GPIO.HIGH)
           GPIO.output(Col3, GPIO.LOW)
        elif light == 14:
           GPIO.output(Row1, GPIO.HIGH)
           GPIO.output(Col4, GPIO.LOW)
        elif light == 21:
           GPIO.output(Row2, GPIO.HIGH)
           GPIO.output(Col1, GPIO.LOW)
        elif light == 22:
           GPIO.output(Row2, GPIO.HIGH)
           GPIO.output(Col2, GPIO.LOW)
        elif light == 23:
           GPIO.output(Row2, GPIO.HIGH)
           GPIO.output(Col3, GPIO.LOW)
        elif light == 24:
           GPIO.output(Row2, GPIO.HIGH)
           GPIO.output(Col4, GPIO.LOW)
          

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
    print("\ndone!\n")


