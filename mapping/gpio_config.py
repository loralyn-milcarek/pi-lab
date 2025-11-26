# gpio_config.py
"""
Central GPIO pin allocation for all projects.
Prevents pin conflicts across sensors.
"""

class GPIOPins:
    """Pin assignments for all sensors"""
    
    # === OUTPUTS (LEDs, Buzzers) ===
    LED = 17       
    BUZZER = 18              # Passive buzzer
    RELAY = 25               # 5V relay module
    
    # === INPUTS (Buttons, Sensors) ===
    BUTTON_1 = 2             # General purpose buttons
    BUTTON_2 = 3
    BUTTON_3 = 4
    TOUCH = 14               # Touch sensor
    
    PIR_MOTION = 15          # Motion sensor
    PHOTO_RESISTOR = 20      # Light sensor
    
    # === DISTANCE SENSORS ===
    ULTRASONIC = 21
    
    # === DIGITAL SENSORS ===
    DHT11_DATA = 16          # Temp/humidity sensor
      
    @classmethod
    def print_allocation(cls):
        """Print all pin assignments for reference"""
        print("=" * 50)
        print("GPIO Pin Allocation Map")
        print("=" * 50)
        for name, pin in vars(cls).items():
            if not name.startswith('_') and isinstance(pin, int):
                print(f"{name:20s} → GPIO {pin:2d}")
        print("=" * 50)