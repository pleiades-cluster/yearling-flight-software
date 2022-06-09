from Big_Test import Face as Face
import time


Face1=Face(4,"y+")
Face2 = Face(0,"x+")
Face1.Sensorinit(Face1.senlist,Face1.address)
'''Face2.Sensorinit(Face2.senlist,Face2.address)
print("init")
print("First Face")
print(Face1.test_all(1,1))
print("-------------------------------------------------------------------")
print("Second Face")
print(Face2.test_all(1,1))'''
Face1.test_all(10,1)