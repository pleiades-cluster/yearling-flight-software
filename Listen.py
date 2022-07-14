from Tasks.template_task import Task
from pycubed import cubesat
import time

class task(Task):
    priority = 3
    frequency = 1
    name='listen'
    color = 'yellow'

    schedule_later=True

    async def main_task(self):
        if cubesat.hardware['Radio1']:
            while True:
                packet = cubesat.radio1.receive()
                if packet is None:
                    pass
                else:
                    print('Received (raw bytes): {0}'.format(packet))
                    rssi = cubesat.radio1.rssi
                    print('Received signal strength: {0} dBm'.format(rssi))