'''
This class creates an object for each face of Yearling. 

Authors: Antony Macar, Michael Pham 
Updated June 3, 2022 
v1
'''  
'''from cgitb import handler'''
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

#I think this is extraneous, put it back if I am wrong
# Create I2C bus as normal
i2c = busio.I2C(board.SCL2, board.SDA2)

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)


class Face:
    def __init__(self, Add, Pos):
        self.address = Add
        self.position = Pos

        #Sensor List Contains Expected Sensors Based on Face
        self.senlist = []
        if Pos == "x+":
            self.senlist.append("MCP")
            self.senlist.append("ADPS")
            self.senlist.append("DRV")
        elif Pos == "x-":
            self.senlist.append("MCP")
            self.senlist.append("ADPS")
            self.senlist.append("DRV")
        elif Pos == "y+":
            self.senlist.append("MCP")
            self.senlist.append("ADPS")
            self.senlist.append("MPU IMU") #Note difference between IMUs 
        elif Pos == "y-":
            self.senlist.append("MCP")
            self.senlist.append("ADPS")
            self.senlist.append("IMU")
        elif Pos == "z+":
            self.senlist.append("MAG")
            self.senlist.append("MCP")
            self.senlist.append("ADPS")
            self.senlist.append("DRV")
            self.senlist.append("COUPLE")
        elif Pos == "z-":
            self.senlist.append("MCP")
            self.senlist.append("ADPS")
        else:
            print("[ERROR] Please input a propper face")

        #This sensors set contains information as to whether sensors are actually working
        self.sensors = { 
            'MCP':      False,
            'ADPS':     False, 
            'DRV':      False,
            'IMU':      False,
            'MPU IMU':  False,
            'BNO IMU':  False, 
            'LSX IMU':  False, 
            'MAG':      False, 
            'COUPLE':   False, 
        }

    # function to initialize all the sensors on that face        
    def Sensorinit(self,senlist,address):

        #Initialize Temperature Sensor
        if "MCP" in senlist:
            try:
                self.mcp = adafruit_mcp9808.MCP9808(tca[address])
                self.sensors['MCP'] = True
                print('[ACTIVE][Temperature Sensor]')
            except Exception as e:
                print('[ERROR][Temperature Sensor]',e)

        #Initialize Light Sensor
        if "ADPS" in senlist:
            try:
                self.light1 = adafruit_apds9960.apds9960.APDS9960(tca[address])
                self.light1.enable_color =True
                self.light1.enable_proximity = True
                self.sensors['ADPS'] = True
                print('[ACTIVE][Light Sensor]')
            except Exception as e: 
                print('[ERROR][Light Sensor]',e)

        #Initialize Motor Driver
        if "DRV" in senlist:
            try:
                self.drv1 = adafruit_drv2605.DRV2605(tca[address])
                self.sensors['DRV'] = True
                print('[ACTIVE][Motor Driver]')
            except Exception as e:
                print('[ERROR][Motor Driver]',e)

        #Initialize MPU IMU 
        if "MPU IMU" in senlist:
            try:
                self.mpu1 = adafruit_mpu6050.MPU6050(tca[address])
                self.sensors['MPU IMU'] = True
                print('[ACTIVE][MPU IMU]')
            except Exception as e:
                print('[ERROR][MPU IMU]',e)
        
        #Initialize Magnetometer
        if "MAG" in senlist:            
            try:
                self.mag1 = adafruit_lis3mdl.LIS3MDL(tca[address])
                self.sensors['MAG'] = True
                print('[ACTIVE][Magnetometer]')
            except Exception as e:
                print('[ERROR][Magnetometer]',e)
                
        #Initialize Thermocouple
        if "COUPLE" in senlist:
            try:
                self.couple1 = adafruit_mcp9600.MCP9600(tca[address]) 
                self.sensors['COUPLE'] = True
                print('[ACTIVE][Thermocouple]')
            except Exception as e:
                print('[ERROR][Thermocouple]',e)

        print('Initialization Complete')

    #Meta Info Getters 
    @property #Gives what sensors should be present
    def senlist_what(self): 
        return self.senlist 
    
    @property #Givens what sensors are actually present 
    def active_sensors(self): 
        return self.sensors

    #Sensor Data Getters 

    @property #Temperature Data Getter
    def temperature(self): 
        if self.sensors['MCP']:
            return self.mcp.temperature
        else:
            print('[WARNING]Temperature sensor not initialized')

    @property #Light Sensor Color Data Getter
    def color_data(self): 
        if self.sensors['ADPS']:
            r1, g1, b1, c1 = self.light1.color_data
            return r1, g1, b1, c1
        else:
            print('[WARNING]Light sensor not initialized')

    #BEWARE: I think none of this motor driver stuff works
    #https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout/python-circuitpython
    #
    #
    @property #Motor Driver Getter 
    def drv_actuate(self, duration): 
        if self.sensors['DRV']:
            print('Actuating Sequence')
            self.drv1.play()
            time.sleep(duration)
            self.drv1.stop()
            print('Actuation Complete')
        else: 
            print('[WARNING]Motor driver not initialized')

    @drv_actuate.setter #I don't know if this is how this actually works
    def drv_actuate(self, sequence): 
        if self.sensors['DRV']:
            print('Encoding Sequence')
            self.drv1.sequence[0] = adafruit_drv2605.Effect(1)
            print('Complete')
        else: 
            print('[WARNING]Motor driver not initialized')
    #
    #
    #
    #BEWARE: NOT WORKING MOTOR DRIVER CODE

    @property #MPU IMU Getter 
    def mpu_data(self):
        if self.sensors['MPU IMU']:
            acel = self.mpu1.acceleration
            gyro = self.mpu1.gyro
            temp = self.mpu1.temperature
            

            return acel,gyro,temp  #Note return is a tuple 
        else:
            print('[WARNING]MPU IMU not initialized')

    @property #Magnetometer Getter 
    def mag(self): 
        if self.sensors['MAG']:
            mag_x, mag_y, mag_z = self.mag1.magnetic
            return mag_x, mag_y, mag_z#Note return is a tuple 
        else:
            print('[WARNING]Magnetometer not initialized')  

    @property #Thermocouple Getter 
    def couple(self): 
        if self.sensors['COUPLE']:
            amb = self.couple1.ambient_temperature
            tip = self.couple1.temperature
            dif = self.couple1.delta_temperature
            return amb, tip, dif #Note return is a tuple 
        else:
            print('[WARNING]Thermocouple not initialized')  

    #Function to test all sensors that should be on each face. 
    #Function takes number of tests "num" and polling rate in hz "rate"
    def test_all(self, num, rate): 

        print('Expected Sensors: ', self.senlist_what)
        print('Initialized Sensors: ', self.active_sensors)
        time.sleep(1) #Remove later for performance boost! 
        print('Initializing Test')

        for i in range(num): 

            print('Test Number: ', i, ' /', num)

            #Test Temperature Sensor
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            if ("MCP" in self.senlist) and (self.sensors.get("MCP") == True):
                try:
                    print('Temperature Sensor')
                    print('Face Temperature: ', self.temperature)
                except Exception as e:
                    print('[ERROR][Temperature Sensor]',e)
            else:
                print('[ERROR]Temperature Sensor Failure')
                
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            #Initialize Light Sensor
            if ("ADPS" in self.senlist) and (self.sensors.get('ADPS') == True ):
                try:
                    print('Light Sensor')
                    print(self.color_data)
                except Exception as e: 
                    print('[ERROR][Light Sensor]',e)
            else:
                print('[ERROR]Light Sensor Failure')
                
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            #Initialize Motor Driver
            if ("DRV" in self.senlist) and (self.sensors.get('DRV') == True ):
                try:
                    print('Motor Driver')
                    print('[ACTIVE][Motor Driver]') #No function defined here yet to use the driver
                except Exception as e:
                    print('[ERROR][Motor Driver]',e)

            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            #Initialize MPU IMU 
            if ("MPU IMU" in self.senlist) and (self.sensors.get('MPU IMU') == True ):
                try:
                    print('MPU IMU')
                    print(self.mpu_data)
                except Exception as e:
                    print('[ERROR][M=PU IMU]',e)
            elif self.position == "x+" or self.position == "x-":
                print()
            else:
                print('[Error]MPU IMU Failure')
            
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            #Initialize Magnetometer
            if ("MAG" in self.senlist) and (self.sensors.get('MAG') == True ):            
                try:
                    print('Magnetometer')
                    print('X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT'.format(self.mag))
                except Exception as e:
                    print('[ERROR][Magnetometer]',e)
            elif self.position == "x+" or self.position== "x-" or self.position == "y+" or self.position == "y-":
                print()
            else:
                print('[Error]Magnetometer Failure')

            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')       
            #Initialize Thermocouple
            if ("COUPLE" in self.senlist) and (self.sensors.get('COUPLE') == True ):
                try:
                    print('Thermocouple')
                    print(self.couple) #Unformatted
                except Exception as e:
                    print('[ERROR][Thermocouple]',e)
            elif self.position == "x+" or self.position== "x-" or self.position == "y+" or self.position == "y-":
                print()
            else: 
                print('[ERROR]Thermocouple Failure')

            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            time.sleep(rate) #Remove later for performance boost! 







