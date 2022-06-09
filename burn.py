# This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
'''import time
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_mcp9808
import adafruit_tca9548a
import mf_initialize'''
from pycubed import cubesat

cubesat.burn(burn_num='2',dutycycle=0.10,duration=2)