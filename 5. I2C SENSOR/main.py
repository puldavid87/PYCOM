import time
from machine import I2C, Pin
from scd30 import SCD30


i2c = I2C(2)
scd30 = SCD30(i2c, 0x61)

while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    while scd30.get_status_ready() != 1:
        time.sleep_ms(200)
    (co2,temp,hum)=scd30.read_measurement()
        #-3
    temp -=3
    print("co2",co2)
    print("temp",temp)
    print("hum",hum)
