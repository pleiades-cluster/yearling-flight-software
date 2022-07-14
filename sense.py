from Tasks.template_task import Task
from Big_Test import Face as Face
import time

class task(Task):
    priority = 2
    frequency = 1/5
    name='sense'
    color = 'blue'

    schedule_later=True

    async def main_task(self):
        Face1=Face(4,"y+")
        Face2 = Face(0,"x+")
        Face3=Face(5,"z-")
        Face4 = Face(1,"z+")
        Face5=Face(2,"x-")
        Face6 = Face(3,"y-")
        print("First Face")
        print(Face1.test_all(1,1))
        print("-------------------------------------------------------------------")
        print("Second Face")
        print(Face2.test_all(1,1))
        print("-------------------------------------------------------------------")
        print("third Face")
        print(Face3.test_all(1,1))
        print("-------------------------------------------------------------------")
        print("fourth Face")
        print(Face4.test_all(1,1))
        print("-------------------------------------------------------------------")
        print("fifth Face")
        print(Face5.test_all(1,1))
        print("-------------------------------------------------------------------")
        print("Sixth Face")
        print(Face6.test_all(1,1))