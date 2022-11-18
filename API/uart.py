import serial

port = "../../../dev/ttyAMA0"
ser = serial.serial_for_url(port, 115200)

def fetch_temperature():
    try: 
        ser.write(b"GET_T")
        temperature = ser.read(4)
        return temperature
    except Exception as e :
        return e

def fetch_pressure():
    try: 
        ser.write(b"GET_P")
        pressure = ser.read(4)
        return pressure
    except Exception as e :
        return e

def fetch_scale():
    try: 
        ser.write(b"GET_K")
        scale = ser.read(4)
        return scale
    except Exception as e :
        return e

def update_scale(x: int):
    try:
        ser.write(b"SET_K")
        ser.write("=" + str(x))
        return x
    except Exception as e:
        return e

def fetch_angle():
    try: 
        ser.write(b"GET_A")
        scale = ser.read(4)
        return scale
    except Exception as e :
        return e
