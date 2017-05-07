import RPi.GPIO as GPIO
import time

print('Distance Measurement In Progress')

GPIO.setmode(GPIO.BCM)
TRIG = 2
ECHO = 3
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# 发送 trig 信号  持续 10us 的方波脉冲
GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)


# 等待低电平结束，然后记录时间。
while GPIO.input(ECHO) == 0：
	pass
pulse_start = time.time()

# 等待高电平结束，然后记录时间。
while GPIO.input(ECHO) == 1:
	pass
pulse_end = time.time()


pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance,2)
print("Distance: {}cm".format(distance))
GPIO.cleanup()

