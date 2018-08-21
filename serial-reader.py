""" Program to read serial input and convert it to JSON format

"""
import serial, sys

def serial_read(port, baud=9600, timeout=None, expected='\n'):
    '''Read a value from port and output it in JSON format

    Keyword arguments:
    port -- device name
    baud -- baudrate, default is 9600 (Available: 2400, 4800, 9600 and 19200)
    timeout -- if None (default): wait forever
               if  0: non-blocking mode, return immediately with zero or more, up to
               the requested number of bytes (not implemented)
               if x: set timeout to x seconds (float allowed), returns immediately if
               the requested number of bytes is available, otherwise wait until their
               timeout expires and return all bytes received until then
               expected: read until this caracter is read (default '\n')

    Returns: (..json..)

    '''

    if baud not in [2400, 4800, 9600, 19200]:
        raise ValueError('baudrate must be 2400, 4800, 9600 or 19200')

    with serial.Serial(port=port, baudrate=baud, timeout=timeout) as ser:
        s = ser.read_until(expected) # bytes
        return s


if __name__ == '__main__':
    for i in range(5):
        print(serial_read(port=sys.argv[1], timeout=3))

