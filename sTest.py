import time
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_mcp9808
import adafruit_mpu6050

from pycubed import cubesat

# Create I2C bus as normal
i2c = busio.I2C(board.SCL2, board.SDA2)

'''# Sensor Init
adps = adafruit_apds9960.apds9960.APDS9960(i2c)
adps.enable_color =True
adps.enable_proximity = True
r, g, b, c = adps.color_data

#Temp Sensor
mcp1 = adafruit_mcp9808.MCP9808(i2c)

#6 DoF IMU
mpu = adafruit_mpu6050.MPU6050(i2c)'''

#Charge Tracking
ichrg = cubesat.charge_current
vbatt = cubesat.battery_voltage
vsys = cubesat.system_voltage
isys = cubesat.current_draw

#while loop for print
while True:

    '''r, g, b, c = adps.color_data

    print('Channel 1 Data')
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    print("")
    print('Temperature: {} degrees C'.format(mcp1.temperature))
    print("")
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    print("")'''
    print('Charge Current: ' + str(cubesat.charge_current()))
    print('Battery Voltage: ' + str(cubesat.battery_voltage))
    print('System Voltage: ' + str(cubesat.system_voltage))
    print('System Current Draw: ' + str(cubesat.current_draw))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(.5)
