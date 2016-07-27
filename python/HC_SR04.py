import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#GPIO_TRIGGER_1 = 23
#GPIO_ECHO_1 = 24
GPIO_TRIGGER_2 = 25
GPIO_ECHO_2 = 18

print "Ultrasonic Measurement"

#GPIO.setup(GPIO_TRIGGER_1,GPIO.OUT)
#GPIO.setup(GPIO_ECHO_1,GPIO.IN)
GPIO.setup(GPIO_TRIGGER_2,GPIO.OUT)
GPIO.setup(GPIO_ECHO_2,GPIO.IN)


#GPIO.output(GPIO_TRIGGER_1, False)
GPIO.output(GPIO_TRIGGER_2, False)


time.sleep(0.5)


#GPIO.output(GPIO_TRIGGER_1, True)
#time.sleep(0.00001)
#GPIO.output(GPIO_TRIGGER_1, False)
#start_1 = time.time()
#while GPIO.input(GPIO_ECHO_1)==0:
#    start_1 = time.time()
#while GPIO.input(GPIO_ECHO_1)==1:
#    stop_1 = time.time()
#elapsed_1 = stop_1-start_1
#distance_1 = elapsed_1 * 34000
#distance_1 = distance_1 / 2

GPIO.output(GPIO_TRIGGER_2, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER_2, False)
start_2 = time.time()
while GPIO.input(GPIO_ECHO_2)==0:
    start_2 = time.time()
while GPIO.input(GPIO_ECHO_2)==1:
    stop_2 = time.time()
elapsed_2 = stop_2-start_2
distance_2 = elapsed_2 * 34000
distance_2 = distance_2 / 2

#print "Distance 1 : %.1f cm" % distance_1
print "Distance 2 : %.1f cm" % distance_2

# Reset GPIO settings
GPIO.cleanup()
