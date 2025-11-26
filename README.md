# pi-lab
Raspberry Pi 5 hardware exploration

---
## Raspberry Pi 5 GPIO Map

| Left GPIO | Left Pin | Right Pin | Right GPIO | Notes |
|-----------|----------|-----------|------------|-------|
| 3V3 | 1 | 2 | 5V | |
| GPIO2 | 3 | 4 | 5V | Button 1 / I2C SDA |
| GPIO3 | 5 | 6 | GND | Button 2 / I2C SCL |
| GPIO4 | 7 | 8 | GPIO14 | Button 3 |
| GND | 9 | 10 | GPIO15 | PIR Motion |
| GPIO17 | 11 | 12 | GPIO18 | LED Simple / Buzzer |
| GPIO27 | 13 | 14 | GND | |
| GPIO22 | 15 | 16 | GPIO23 | LED Red / LED Yellow |
| 3V3 | 17 | 18 | GPIO24 | LED Green |
| GPIO10 | 19 | 20 | GND | SPI MOSI |
| GPIO9 | 21 | 22 | GPIO25 | SPI MISO / Relay |
| GPIO11 | 23 | 24 | GPIO8 | SPI CLK / SPI CS |
| GND | 25 | 26 | GPIO7 | |
| GPIO0 | 27 | 28 | GPIO1 | Reserved (EEPROM) |
| GPIO5 | 29 | 30 | GND | |
| GPIO6 | 31 | 32 | GPIO12 | |
| GPIO13 | 33 | 34 | GND | RGB Red |
| GPIO19 | 35 | 36 | GPIO16 | RGB Green / DHT11 |
| GPIO26 | 37 | 38 | GPIO20 | RGB Blue / Ultrasonic Trigger |
| GND | 39 | 40 | GPIO21 | Ultrasonic Echo |