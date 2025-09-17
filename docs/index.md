# Welcome to Luna

Welcome to the official documentation for the **Luna** project.

For a full API reference, please visit the [API Reference](reference/index.md) section.

## Quick Start

Here's a quick example to get you started:

```python
from luna.led_controller import LEDController
import time

led = LEDController(pin=9)

try:
    print("Blinking the LED...")
    led.blink(times=5, delay=1)
finally:
    led.cleanup()