from pycubed import cubesat
import time

ichrg = cubesat.charge_current
vbatt = cubesat.battery_voltage

while True:
    print('Charge Current: ' + str(cubesat.charge_current()))
    print('Battery Voltage: ' + str(cubesat.battery_voltage))

    time.sleep(2)
