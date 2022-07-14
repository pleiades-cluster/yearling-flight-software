from Tasks.template_task import Task
from pycubed import cubesat
import time

class task(Task):
    priority = 2
    frequency = 5
    name='talk'
    color = 'red'

    schedule_later=True

    async def main_task(self):
        count = 0
        if cubesat.hardware['Radio1']:
            while count < 10:
                count += 1
                print('Sending Message...'+str(count))
                cubesat.radio1.send('Hello World: '+str(count))
                time.sleep(2)