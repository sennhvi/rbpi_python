import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


# no MCP3008, just learn a bit
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)  # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3  # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1  # first bit is 'null' so drop it
    return adcout


SPICLK = 4
SPIMISO = 17
SPIMOSI = 18
SPICS = 23

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

ldr_adc = 0;

last_read = 0
tolerance = 5

while True:
    # we'll assume that the light didn't change
    input_changed = False

    # read the analog pin
    ldr_value = readadc(ldr_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    ldr_movement = abs(ldr_value - last_read)

    if (ldr_movement > tolerance):
        input_changed = True

    if (input_changed):
        print('Light = ', int(ldr_value))
        last_read = ldr_value

    # hang out and do nothing for a half second
    time.sleep(0.5)
