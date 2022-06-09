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
import adafruit_mpu6050
import adafruit_lis3mdl
import adafruit_lis3mdl
import adafruit_drv2605
import adafruit_mcp9600
import digitalio
from pycubed import cubesat

# Create I2C bus as normal
i2c = busio.I2C(board.SCL2, board.SDA2)

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)


spresense = digitalio.DigitalInOut(board.PB17)
spresense.direction = digitalio.Direction.OUTPUT

spresense.value = False



#vsolar
ichrg = cubesat.charge_current()
vsys = cubesat.system_voltage





# side 1'
'''mpu1 = adafruit_mpu6050.MPU6050(tca[1])'''
mag1 = adafruit_lis3mdl.LIS3MDL(tca[1])

couple1 = adafruit_mcp9600.MCP9600(tca[1])

sensor1 = adafruit_apds9960.apds9960.APDS9960(tca[1])
sensor1.enable_color =True
sensor1.enable_proximity = True
mcp1 = adafruit_mcp9808.MCP9808(tca[1])
drv1 = adafruit_drv2605.DRV2605(tca[1])
'''mag_x, mag_y, mag_z = mag1.magnetic'''







'''
#side 2
sensor2 = adafruit_apds9960.apds9960.APDS9960(tca[4])
sensor2.enable_color =True
r2, g2, b2, c2 = sensor2.color_data
mcp2 = adafruit_mcp9808.MCP9808(tca[4])
mpu2 = adafruit_mpu6050.MPU6050(tca[4])



#side 3
sensor3 = adafruit_apds9960.apds9960.APDS9960(tca[1])
sensor3.enable_color =True
r3, g3, b3, c3 = sensor3.color_data
mcp3 = adafruit_mcp9808.MCP9808(tca[1])
mag1 = adafruit_lis3mdl.LIS3MDL(tca[1])
drv2 = adafruit_drv2605.DRV2605(tca[1])


#side 4
sensor4 = adafruit_apds9960.apds9960.APDS9960(tca[0])
sensor4.enable_color =True
r4, g4, b4, c4 = sensor4.color_data
mcp4 = adafruit_mcp9808.MCP9808(tca[0])
mpu4 = adafruit_mpu6050.MPU6050(tca[0])



#side 5
sensor5 = adafruit_apds9960.apds9960.APDS9960(tca[2])
sensor5.enable_color =True
r5, g5, b5, c5 = sensor5.color_data
mcp5 = adafruit_mcp9808.MCP9808(tca[2])
drv5 = adafruit_drv2605.DRV2605(tca[2])




#side 6
sensor6 = adafruit_apds9960.apds9960.APDS9960(tca[5])
mcp6 = adafruit_mcp9808.MCP9808(tca[5])


'''


#while loop for print# Write your code here :-)

def Face1():
    sensor1.enable_color =True
    r1, g1, b1, c1 = sensor1.color_data
    '''drv1.sequence[0] = adafruit_drv2605.Effect(1)
    drv1.play()'''
    print('Channel 1 Data')
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r1, g1, b1, c1))
    print('Temperature: {} degrees C'.format(mcp1.temperature))
    '''print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu1.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu1.gyro))
    print("Temperature: %.2f C" % mpu1.temperature)
    print("")'''
    mag_x, mag_y, mag_z = mag1.magnetic
    print('X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT'.format(mag_x, mag_y, mag_z))
    print((couple1.ambient_temperature, couple1.temperature, couple1.delta_temperature))

    ichrg = cubesat.charge_current()
    print(ichrg)
    print(vsys)
    time.sleep(1)

def Face2():

    sensor2.enable_color =True
    r2, g2, b2, c2 = sensor2.color_data
    print('Channel 2 Data')
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r2, g2, b2, c2))
    print('Temperature: {} degrees C'.format(mcp2.temperature))
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu2.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu2.gyro))
    print("Temperature: %.2f C" % mpu2.temperature)
    print("")
    print(ichrg)
    print(vsys)
    time.sleep(2)


def Face3():

    sensor3.enable_color =True
    r3, g3, b3, c3 = sensor3.color_data
    print('Channel 3 Data')
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r3, g3, b3, c3))
    print('Temperature: {} degrees C'.format(mcp3.temperature))
    mag_x1, mag_y1, mag_z1 = mag1.magnetic
    print('X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT'.format(mag_x1, mag_y1, mag_z1))
    time.sleep(2)

def Face4():

    sensor4.enable_color =True
    r4, g4, b4, c4 = sensor4.color_data
    print('Channel 4 Data')
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r4, g4, b4, c4))
    print('Temperature: {} degrees C'.format(mcp4.temperature))
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu4.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu4.gyro))
    print("Temperature: %.2f C" % mpu4.temperature)
    print("")
    time.sleep(2)

def Face5():

    sensor5.enable_color =True
    r5, g5, b5, c5 = sensor5.color_data
    print('Channel 5 Data')
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r5, g5, b5, c5))
    print('Temperature: {} degrees C'.format(mcp5.temperature))
    drv5.sequence[0] = adafruit_drv2605.Effect(1)
    drv5.play()
    time.sleep(2)

'''def FaceOn(face):
    try:
        while True:
            face()
    except KeyboardInterrupt:
        print('Terminated!')
  '''
def yes():
    try:
        x = input(" What face do you want?  ")
        if x ==  "1":
            while True:
                Face1()
        elif x == "2":
            while True:
                Face2()
        elif x == "3":
            while True:
                Face3()
        elif x == "4":
            while True:
                Face4()
        elif x == "5":
            while True:
                Face5()
        else:
            print("Please input a value between 1-5 !!!! :(")


    except KeyboardInterrupt:
            print('Terminated!')

while True:
    yes()
