from pycubed import cubesat

while True:
    data = cubesat.uart.read(255)  # read up to 32 bytes
    # print(data)  # this is a bytearray type
    print(cubesat.uart.in_waiting)
    print(data)
    if data is not None:

        # convert bytearray to string
        data_string = ''.join([chr(b) for b in data])
        print(data_string, end="")