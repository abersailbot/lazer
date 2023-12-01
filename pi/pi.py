#Author Dan Cook - 30/11/2023

#Original Source: https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/#UART_protocol

#import modules
import serial #Documentation can be found here: https://pyserial.readthedocs.io/en/latest/shortintro.html
import time

#initialise and set global constants
BAUDRATE = 9600
ARDUINOPATH = '/dev/ttyUSB0'
SERIALPORTTIMEOUT = False;
try:
    ARDUINOPISERIALPORT = serial.Serial(ARDUINOPATH, BAUDRATE, timeout=1); #creates an instance of the serial class maybe?

except serial.SerialException as serialException:
    print(serialException)
    print("ARDUINOPISERIALPORT could not be set. Is the path correct? On linux the path should be something like '/dev/tty*' where * is (probably USB0 or) any combination of any characters. On windows the path should be something like 'com{d}' where {d} is 1 or more digits \nThe serial documentation is linked at the top of the file");
    
    exit()
    
#param1 -> the data that will be transmitted. NOTE: the string must already be converted into bytes.
          #This can be done with the character b before the opening speech mark like this ``` b"my string" ``` or
          #by using the bytes function like this ``` bytes(data, 'utf-8') ``` or
          #by using the str.encode() function like this ``` "my string".encode('utf-8') ``` or ``` "my string".encode('ascii') ```
#param2 -> the serial port that will be written to
def transmitData(data: str, serialPort: serial) -> None:
    serialPort.write(data)

#param1 -> the serial port that will receive the data
def getData(serialPort: serial) -> str:
    SERIALPORTTIMEOUT = False;
    data = serialPort.readline().decode('utf-8').rstrip();
    SERIALPORTTIMEOUT = not data.endswith('\n')
    return data

#param1 -> processes the data
#notes: maybe use a switch statement or regex to figure out how the data should be processed
def processData(data: str) -> None:
    print("\"" + data + "\"")



#note: the first time the main function runs the function getData(serialPort: serial) returns an empty string. I think this is a problem with the arduino code or maybe hardware timing because the problem appears regularly but is inconsistent where it appears - Dan C
def main():
    whileLoopCounter = 0
    ARDUINOPISERIALPORT.reset_input_buffer()
    
    while True:
        print(whileLoopCounter)
        
        #param 1 -> symbol b converts string into bytes
        transmitData(b"THIS STRING\n", ARDUINOPISERIALPORT)
        data = getData(ARDUINOPISERIALPORT)
        
          
        processData(data)
        
        time.sleep(1)
        whileLoopCounter = whileLoopCounter + 1

if __name__ == '__main__':
    main()