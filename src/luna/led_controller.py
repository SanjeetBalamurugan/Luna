import RPi.GPIO as GPIO
import time

class LEDController:
    def __init__(self, pin=18):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def blink(self, times=5, delay=1):
        for _ in range(times):
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(delay)

    def cleanup(self):
        GPIO.cleanup()
