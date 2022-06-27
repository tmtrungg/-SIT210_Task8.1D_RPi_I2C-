import smbus
import time

# Constants
DEVICE     = 0x23 # I2C address
POWER_DOWN = 0x00 # Power off
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data value

# Default 1lx resolutionand 120ms
DEFAULT_MODE = 0x20

bus = smbus.SMBus(1)

def convertToNumber(data):
  #convert 2 byte data into decimal number
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
    # Input i2c sensor of light level
    data = bus.read_i2c_block_data(addr,DEFAULT_MODE)
    input = convertToNumber(data)
    if ( input < 20 ):
      return "Too dark"
    if (( input >= 20 ) and ( input < 50 )):
      return "Dark"
    if (( input >= 50 ) and ( input < 100 )):
      return "Medium"
    if (( input >= 100 ) and ( input < 200 )):
      return "Bright"
    if ( input >= 200 ):
      return "Too bright"

while True:
    result = readLight()
    print("Light Level : " + str(result))
    time.sleep(0.5)
