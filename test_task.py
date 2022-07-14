

'''from Tasks.template_task import Task
import time

class task(Task):
    priority = 4
    frequency = 1/30 # once every 30s
    name = 'test'
    color = 'gray'

    schedule_later = True

    async def main_task(self):
        self.debug('test start: {}'.format(time.monotonic()))
        await self.cubesat.tasko.sleep(10)
        self.debug('test stop: {}'.format(time.monotonic()))'''

# Blink the RGB LED

from Tasks.template_task import Task
from Big_Test import Face as Face
import time

class task1(Task):
    priority = 255
    frequency = 2 # twice per second
    name='blink'
    color = 'pink'

    rgb_on = False
    async def main_task(self):
        if self.rgb_on:
            self.cubesat.RGB=(0,0,0)
            self.rgb_on=False
        else:
            self.cubesat.RGB=(0,255,0)
            self.rgb_on=True

class task2(Task):
    priority = 1
    frequency = 1/5
    name='sense'
    color = 'blue'

    schedule_later=True

    async def main_task(self):
        Face1=Face(4,"z+")
        Face2 = Face(0,"x+")
        Face1.Sensorinit(Face1.senlist,Face1.address)
        Face2.Sensorinit(Face2.senlist,Face2.address)
        print("init")
        print("First Face")
        print(Face1.test_all(1,1))
        print("-------------------------------------------------------------------")
        print("Second Face")
        print(Face2.test_all(1,1))



