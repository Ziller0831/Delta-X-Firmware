import serial
import time

ser = serial.Serial('/dev/MEGA2560', 115200, timeout=1)  # open serial port
time.sleep(2)
print(ser.readline())

gcodes = []
gcodes.append('G28')
gcodes.append('G01 Z-550')
gcodes.append('G01 X200')
gcodes.append('G01 X200 Y200')
gcodes.append('G01 Y200')
gcodes.append('G01 X200')
# gcodes.append('G01 Y100')
# gcodes.append('G01 X100')
# gcodes.append('G01 Y-100')
# gcodes.append('G01 X-100')
# gcodes.append('G01 X100')
# gcodes.append('G01 Y0')
# gcodes.append('G01 X0')
# gcodes.append('G01 Z-700')
# gcodes.append('G01 Z-450')

for gcode in gcodes:
    print(gcode)
    ser.write((gcode + '\n').encode())
    while 1:
        response = ser.readline()
        print(response)
        if (response.find('Ok'.encode()) > -1):
            break
        elif (response.find('Unknown'.encode()) > -1):
            break

ser.close()             # close port
