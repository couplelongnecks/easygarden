#dead simple auto garden project using the esp32, 3.3v water pump, relay and DFR capacitive sensor SEN0193
#by couplelongnecks

from machine import Pin, ADC
from time import sleep

ADC_PIN = 32
RELAY_PIN = 14

adc_moisture = ADC(Pin(ADC_PIN, Pin.IN))
relay = Pin(RELAY_PIN, Pin.OUT)
adc_moisture.atten(3)

waterValue = 21300 # Replace with the value you get when sensor is in cup of water
airValue = 46600

intervals = (airValue - waterValue)/3
soilMoistureValue = 0

while True:
    soilMoistureValue = adc_moisture.read_u16()
    #print('raw reading: ' + str(soilMoistureValue)) #Uncomment this to find your waterValue and airValue while testing
    
    if(soilMoistureValue > waterValue and soilMoistureValue < (waterValue + intervals)):
        relay(0)
        print('Very Wet')
    elif(soilMoistureValue > (waterValue + intervals) and soilMoistureValue < (airValue - intervals)):
        relay(0)
        print('Wet')
    elif(soilMoistureValue < airValue and soilMoistureValue > (airValue - intervals)):
        relay(1)
        print('Dry')
    sleep(0.2)
