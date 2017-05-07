# ！/user/bin/env python
# encoding:utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

GPIO.output(3,False)

#创建一个 pwm 实例，需要两个参数，第一个是 GPIO 引脚号，这里用 2 引脚
#第二个是频率(HZ),频率越高 LED 看上去越不会闪烁，相应地对 CPU 要求就越高
pwm = GPIO.PWM(2,80)

pwm.start(0)

while True:
	# 电流从小到大，LED从暗到亮
	for i in range(0,101,1):
			pwm.ChangeDutyCycle(i) #占空比在 0% - 100% 间递增变化
			time.sleep(.02)

	# 电流从大到小，LED从亮到暗
	for i in range(100,-1,-1):
			pwm.ChangeDutyCycle(i) # 占空比在 100% - 0% 间递减变化
			time.sleep(.02)