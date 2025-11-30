#!/usr/bin/env python3
"""
Simple LED toggle control with button.

Button behaviors:
- Short press (< 2 seconds): Toggle LED on/off
- Long press (>= 2 seconds): Blink LED 3 times, then turn off
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from gpiozero import LED, Button
from mapping.gpio_config import GPIOPins
import time

class ButtonLEDControl:
    """Control LED with button input"""
    
    def __init__(self):
        """Initialize LED and button from central GPIO config"""
        try:
            self.led = LED(GPIOPins.LED)
            self.button = Button(GPIOPins.BUTTON_1)
            self.led_state = False  # Track LED state (on/off)
            self.button_press_time = None
            self.long_press_detected = False
            
            # Attach button event handlers
            self.button.when_pressed = self.on_button_press
            self.button.when_released = self.on_button_release
            
            print("✓ LED and Button initialized successfully")
            print(f"  LED on GPIO {GPIOPins.LED}")
            print(f"  Button on GPIO {GPIOPins.BUTTON_1}")
            print("\nButton Controls:")
            print("  • Short press (< 2s): Toggle LED on/off")
            print("  • Long press (>= 2s): Blink 3 times, then turn off")
            print("\nPress Ctrl+C to exit\n")
        except Exception as e:
            print(f"❌ Error initializing hardware: {e}", file=sys.stderr)
            sys.exit(1)
    
    def on_button_press(self):
        """Handle button press event"""
        self.button_press_time = time.time()
        self.long_press_detected = False
    
    def on_button_release(self):
        """Handle button release event"""
        if self.button_press_time is None:
            return
        
        press_duration = time.time() - self.button_press_time
        
        if press_duration >= 2.0:
            # Long press: blink 3 times then turn off
            self.blink_led()
        else:
            # Short press: toggle LED
            self.toggle_led()
    
    def toggle_led(self):
        """Toggle LED on/off"""
        if self.led_state:
            self.led.off()
            self.led_state = False
            print("🔴 LED OFF")
        else:
            self.led.on()
            self.led_state = True
            print("🟢 LED ON")
    
    def blink_led(self):
        """Blink LED 3 times, then turn off"""
        print("✨ Blinking LED 3 times...")
        for i in range(3):
            self.led.on()
            time.sleep(0.3)
            self.led.off()
            time.sleep(0.3)
            print(f"  Blink {i+1}/3")
        self.led_state = False
        print("🔴 LED OFF")
    
    def run(self):
        """Keep the program running"""
        try:
            # Keep the program running indefinitely
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n\nShutting down...")
            self.led.off()
            self.button.close()
            self.led.close()
            print("✓ Cleanup complete")
            sys.exit(0)

if __name__ == "__main__":
    control = ButtonLEDControl()
    control.run()
