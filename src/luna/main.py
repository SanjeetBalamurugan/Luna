"""
main.py

Entry point for the Raspberry Pi project.
"""

from luna.hello import hello_world
from luna.led_controller import LEDController

def main():
    """Main function that runs the project."""

    led = LEDController(pin=9)
    led.blink()
    led.cleanup()
    hello_world()

if __name__ == "__main__":
    main()
