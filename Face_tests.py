import Big_Data as b
count=0
print("Initializing Hardware")
Face1=b.Face(5,"y-")
Face2 = b.Face(4,"y+")
Face3=b.Face(3,"x-")
Face4 = b.Face(2,"z+")
Face5=b.Face(1,"z-")
Face6 = b.Face(0,"x+")
if(count==0):
    Face1.Sensorinit(Face1.senlist,Face1.address)
    Face2.Sensorinit(Face2.senlist,Face2.address)
    Face3.Sensorinit(Face3.senlist,Face3.address)
    Face4.Sensorinit(Face4.senlist,Face4.address)
    Face5.Sensorinit(Face5.senlist,Face5.address)
    Face6.Sensorinit(Face6.senlist,Face6.address)
    print("init")
print("init")
print("First Face")
face1=Face1.test_all(1,1)
print(face1)
print("-------------------------------------------------------------------")
print("Second Face")
face2=Face2.test_all(1,1)
print(face2)
print("-------------------------------------------------------------------")
print("third Face")
face3=Face3.test_all(1,1)
print(face3)
print("-------------------------------------------------------------------")
print("fourth Face")
face4=Face4.test_all(1,1)
print(face4)
print("-------------------------------------------------------------------")
print("fifth Face")
face5=Face5.test_all(1,1)
print(face5)
print("-------------------------------------------------------------------")
print("Sixth Face")
face6=Face6.test_all(1,1)
print(face6)