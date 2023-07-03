import binascii
import struct
import temphumid
import lightsensor
from machine import Pin, ADC
import time
from loraWan import lora

lora = lora()

# Pin setups
pinTempHumid = Pin(13)
pinLightSensor = Pin(27)
ldr = ADC(pinLightSensor)
led = Pin("LED", Pin.OUT)

# Helium
DEV_EUI = "6081F9A322D168C7"
APP_EUI = "6081F9AC4E762489"
APP_KEY = "ACD5CA3941DD27F4CDCA786BFE575260"

lora.configure(DEV_EUI, APP_EUI, APP_KEY)

lora.startJoin()
print("Start Join.....")
while not lora.checkJoinStatus():
  print("Joining....")
  time.sleep(1)
print("Join success!")
led.on()

while True:

  temperature, humidity = temphumid.temphumid(pinTempHumid)

  darkness = lightsensor.lightCheck(ldr, led)

  print(darkness)

  if temperature > 21 and darkness <= 2.5:
    blindState = int(1)
  else:
    blindState = int(0)

  temperature_int = int(temperature * 10)
  humidity_int = int(humidity * 10)
  darkness_int = int(darkness * 10)

  print(darkness_int)

  if humidity_int < 0:
    humidity_int = 0

  if darkness_int < 0:
    darkness_int = 0

  payload = struct.pack(">hHHb", temperature_int, humidity_int, darkness_int, blindState)
  payload = binascii.hexlify(payload).decode("utf-8")

  lora.sendMsg(payload)
  print("Sent message:", payload)

  response = lora.receiveMsg()

  if response != "":
    print("Received: ", end=": ")
    print(response) 

  # Duration of sleep in seconds
  sleep_duration = 60 * 60  # 60 minutes in seconds

  time.sleep(sleep_duration)

