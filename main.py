from machine import Pin, I2C
import time
from pico_i2c_lcd import I2cLcd

# Define the LCD Display
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
lcd = I2cLcd(i2c, i2c.scan()[0],2,16)

# Define the pins where the sensor is connected
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

def get_distance():
    # Send a 10-microsecond pulse.
    trigger.low()
    time.sleep_us(2)  # Wait for 2 microseconds low pulse
    trigger.high()
    time.sleep_us(10)  # Keep the trigger high for 10 microseconds
    trigger.low()

    # Wait for the pulse on the echo pin.
    while echo.value() == 0:
        pass
    start = time.ticks_us()

    # Measure the duration of the high pulse.
    while echo.value() == 1:
        pass
    finish = time.ticks_us()

    # Calculate the distance in centimeters and return it.
    return round ((finish - start) / 58)

while True:
    lcd.clear()
    lcd.putstr("distance:"+ str(get_distance())+ " cm")
    time.sleep(1)

