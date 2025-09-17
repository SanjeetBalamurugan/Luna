import RPi.GPIO as GPIO
import time

class LEDController:
    """A class to control an LED connected to a Raspberry Pi GPIO pin.

    This class provides methods to initialize, control, and clean up
    the GPIO pin used for an LED.

    Args:
        pin (int, optional): The GPIO pin number in BCM mode. Defaults to 18.
    """
    def __init__(self, pin=18):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def blink(self, times=5, delay=1):
        """Blinks the LED a specified number of times with a given delay.

        Args:
            times (int, optional): The number of times to blink the LED.
                Defaults to 5.
            delay (int, optional): The delay in seconds between blinks.
                Defaults to 1.
        
        Example:
            ```python
            from luna.led_controller import LEDController
            import time

            # Create an instance of the LEDController
            led = LEDController(pin=18)
            
            # Blink the LED 5 times with a 1-second delay
            led.blink(times=5, delay=1)
            
            # Note: A real-world application would use a try...finally block for cleanup
            ```
        """
        for _ in range(times):
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(delay)

    def cleanup(self):
        """Cleans up the GPIO settings.

        This should be called at the end of the script to release the
        GPIO pin and prevent potential errors in future programs.
        
        Example:
            ```python
            from luna.led_controller import LEDController

            led = LEDController(pin=18)
            
            try:
                # Run some code that uses the LED
                led.blink(times=2)
            finally:
                # Always clean up the GPIO settings
                led.cleanup()
            ```
        """
        GPIO.cleanup()