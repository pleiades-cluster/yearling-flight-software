from pycubed import cubesat 
import time

yagiMode = False
#testMsg = "According to all known laws of aviation, there is no way a bee should be able to fly."
#testMsg = "Its over Anakin I have the high ground!"
testMsg = "I have brought peace, freedom, justice, and security to my new empire. Your new empire!?"
#testMsg = "Hello There!"

cubesat.radio1.spreading_factor=11
cubesat.radio1.tx_power=13
cubesat.radio1.low_datarate_optimize=True
cubesat.radio1.node=0xFA
cubesat.radio1.destination=0xFB

def yagiSide(): 
    print("Listening for transmissions, 10s")
    response = cubesat.radio1.receive(keep_listening=True)

    if response is not None:
        print("packet received")
        print('msg: {}, RSSI: {}'.format(response,cubesat.radio1.last_rssi),2)

        time.sleep(1)

        cubesat.radio1.send('Echo:{}'.format(cubesat.radio1.last_rssi))
        print("Echo sent")
        time.sleep(1)

def fieldSide():
    print("Sending test message:")
    cubesat.radio1.send(testMsg + " SF: " + str(cubesat.radio1.spreading_factor), keep_listening=True)

    print("Listening for transmissions, 10s")
    heard_something = cubesat.radio1.await_rx(timeout=10)

    if heard_something:
            response = cubesat.radio1.receive(keep_listening=True)
            if response is not None:
                print("packet received")
                print('msg: {}, RSSI: {}'.format(response,cubesat.radio1.last_rssi-137),2)

    time.sleep(5)


while True:
    if yagiMode: 
        yagiSide()

    else: 
        fieldSide()