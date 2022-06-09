# This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_mcp9808
import adafruit_tca9548a
import mf_initialize
from pycubed import cubesat


count = 0
if cubesat.hardware['Radio1']:
    while True:
        count += 1
        print('Sending Message...'+str(count))
        cubesat.radio1.send('Hello World: '+str(count))
        time.sleep(2)