from Tasks.template_task import Task
from Big_Test import Face as Face
import time

class task(Task):
    priority = 1
    frequency = 1/5
    name='initialization'
    color = 'green'
    count=0 #variable to check if sensors have been initialized

    schedule_later=True

    async def main_task(self):
        print("Initializing Hardware")
        Face1=Face(4,"y+")
        Face2 = Face(0,"x+")
        Face3=Face(5,"z-")
        Face4 = Face(1,"z+")
        Face5=Face(2,"x-")
        Face6 = Face(3,"y-")
        if(self.count==0):
            Face1.Sensorinit(Face1.senlist,Face1.address)
            Face2.Sensorinit(Face2.senlist,Face2.address)
            Face3.Sensorinit(Face3.senlist,Face3.address)
            Face4.Sensorinit(Face4.senlist,Face4.address)
            Face5.Sensorinit(Face5.senlist,Face5.address)
            Face6.Sensorinit(Face6.senlist,Face6.address)
            print("init")
        print("init")
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
        
        