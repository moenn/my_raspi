import time
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)
beep = 2
GPIO.setup(beep,GPIO.OUT)

#蜂鸣器每 n s 响一次
def beep_frequ(t):
	while True:
		GPIO.output(beep,True)
		GPIO.output(beep,False)
		time.sleep(t)



beep_frequ(10)