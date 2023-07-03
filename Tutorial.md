# Temperature, humidity and brightness tracker for blinds.
An IoT project by Erik Borgström (eb223fe).

---

### Overview
This report presents the procedure for the project done during the IoT summercourse 2023. The report will consist of material used, some code snippets, and detailed explanation for how to make it yourself. At start the project was supposed to automate the blinds, rolling them down when it's to warm and bright inside the living room. Unfortunately my blinds at home did not support it, and I will have to buy some new ones in the future, continuing this project. So for now, it will send an email, recommending the user if the blinds should be up or down for the perfect environment in the room.
Following this tutorial it wont take to long doing it. I would estimate 5 hours, setting the Pico up, your workspace, and connect all of the hardware.

## Objective
The summer gets hot in Sweden from time to time, and our apartments designed for cold Swedish winters it does not get better on the inside. If the sun is constantly beaming through the windows, the inside environment quickly becomes unbearable, with this project we aim to make the environment better on the inside, by trying to block out the sun when it is the strongest. A problem is best to tackle before it has happened, so with this we try to block out the sun before the room gets to hot, ultimately requiring us to use more energy to cool it down.


## Material

---

### List of Materials 
| IoT Device| Link     | Price |
| --------  | -------- | -------- |
|Pi Pico WH |[electrokit](https://www.electrokit.com/produkt/raspberry-pi-pico-wh/)|109.00 SEK|
|Photoresistor|[electrokit](https://www.electrokit.com/produkt/ljussensor/)| 39.00 SEK|
|DHT11 Humidity & Temperature Sensor|[electrokit](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/)| 49.00 SEK|
|Breadboard|[electrokit](https://www.electrokit.com/produkt/kopplingsdack-840-anslutningar/)| 69.00 SEK|
|LoRaWAN|[elfa distrelec](https://www.elfa.se/sv/asr6501-868-mhz-lorawan-kommunikationsenhet-med-antenn-m5stack-u117/p/30221929?ext_cid=shgooaqsesv-Shopping-PerformanceMax-CSS&&cq_src=google_ads&cq_cmp=18208288444&cq_con=&cq_term=&cq_med=pla&cq_plac=&cq_net=x&cq_pos=&cq_plt=gp)| 200.00 SEK|

---

![Pico WH](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/Pico.png)
*<p style="text-align: center;">Fig.1. Raspberry Pi Pico WH</p>*

This is the Pico microcontroller used in this tutorial, it is a cheap microcontroller allowing you to make a ton of different projects. It has built in wireless network. But as we wanted to learn more about IoT we are using the LoRaWAN in this tutorial and not the built in wireless. 

![Breadboard](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/breadBoard.png)
*<p style="text-align: center;">Fig.2. Breadboard</p>*

This is the board where everything will be connected.

![LoRaWAN](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/LoRaWAN.png)
*<p style="text-align: center;">Fig.3. LoRaWAN</p>*

LoRaWAN is what we will use instead of the built in wireless. This is used for long range communication of small data. This project does not specifically need it as we will use it inside at all time, but it was used to learn more of IoT.

![Temperature & Humidity](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/DH11.png)
*<p style="text-align: center;">Fig.4. DHT11</p>*

This is our temperature and humidity reader, it reads the surrounding areas temperature and humidity. 

The pin next to the S is the data pin, the middle is the power and the furthest right is the ground.

The use of DHT11 is solely for more data, as it comes with humidity, as we want to be able to see the current environment in the room as well. The project could be done with only a temperature reader as well, that does not include humidity.

![Lightsensor](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/lightsensor.png)
*<p style="text-align: center;">Fig.5. Photoresistor</p>*

The photoresistor used to collect that brightness of the room, this to make sure that even if it might be to hot, we will not have the blinds down if it is dark outside.

The pin next to the S is the data pin, the middle is the power and the furthest right is the ground.

---

## Computer setup

As VS Code was already installed on my computer and it's my favorite IDE it was an easy choice. This project has been done on a Windows computer, and the tutorial is therefore limited to that operating system. If you use another system, there might be other steps that is needed to be done that is not covered in this tutorial.
To proceed make sure you install VS Code, Node.js and Pymakr.

---

### IDE installation

* [Node js](https://nodejs.org/en)
Select the most current version.
* [VS Code](https://code.visualstudio.com/)

When the downloads are finished make sure to install both of the software. When the installation is complete launch VS Code and open up the extension tab.

![VS Code Extension tab](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/VSCodeExstensionTab.png)
*<p style="text-align: center;">Fig.6. Extension tab VS Code</p>*

The icon of the extension tab is displayed as purple.
Install the Pymakr extension and restart VS Code.

The Pymakr icon should now be displayed and available for you to open.
![Pymakr icon](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/Pymkr.png)
*<p style="text-align: center;">Fig.7. Pymakr VS Code</p>*

---

### Firmware

Now it is time to update the Pico microchip to make sure that it runs micropython.
Make sure that the IDE installation has been successfully completed first.

1. Download the firmware uf2 file [here](https://micropython.org/download/rp2-pico-w/).
Make sure that the latest version in the Releases category is selected and not the Nightly builds.
2. Connect the micro-USB into your raspberry pi. Make sure to be careful when inserting it. 
3. Now hold down the BOOTSEL button as you insert the other end of the cable into your computer USB.
   
![BOOTSEL](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/bootsel.png)
*<p style="text-align: center;">Fig.8. BOOTSEL Button</p>*
4. Now you should see a new file storage in your file system named RPI-RP2, open it up and drag the uf2 file there.
5. Your board will disconnect automatically and then reconnect. Do not disconnect the device before the firmware installation is complete.

Now it is time to test the board. 
Create a project in the Pymakr plugin by pressing the plus icon inside the extension. 
Connect the Pico by pressing the lightning button next to the name.  

![Lightning Button](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/lightning.png)
*<p style="text-align: center;">Fig.9. Lightning Button.</p>*
When that is done press the "create terminal" button.
![Create Terminal](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/Terminalbutton.png)
*<p style="text-align: center;">Fig.10. Create Terminal Button.</p>*

When that is done you should see >>> symbols in the terminal.
Type this in:
```micropython
print("We are doing Erik Borgstrom's tutorial.")
```
![Result of print](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/print.png)
*<p style="text-align: center;">Fig.11. The result of the test.</p>*

if as shown in the picture the text is printed back to you, you have successfully installed the IDE, Pymakr, Node js and updated the firmware on your microchip.

---

### Uploading files
Now it is time to upload files to your Pico.
After the Pico is connected it should look something like this.
![Pymakr](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/PymakrWithDevice.png)
*<p style="text-align: center;">Fig.12. Pymakr exstension with Pico connected.</p>*

You can then go to your project files by pressing explorer, it is the top left button with two papers stacked on each other.

If you are in the right folder it should look something like this except that you wont have all the files, the only file you should have is pymakr.conf.  

![Explorer](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/Explorer.png)
*<p style="text-align: center;">Fig.13. File explorer.</p>*

Now create a file and call it main.py and paste this code
```micropython
print("We are doing Erik Borgstrom's tutorial.")
```

When that is done save the file by pressing CTRL-S. Navigate back to the Pymakr extesntion and press the "Sync project to device" button by hovering over your device under you project.
Now you have uploaded your files to your Pico.

Notice that if you hover over the project name instead you have a button looking like this </>. If you press it the development mode is started and Pymakr will automatically update your Pico every time you save your files. This so that you can continuously test the program as you are programming.

## Putting everything together

---

### Rasberry Pi Pico

Let us start by familiarize ourselves with the layout of the Pico, this layout map will be used throughout this tutorial.

![Pi Pico](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/PicoTemplate.png)
*<p style="text-align: center;">Fig.14. Pico Layout.</p>*

---

### Circuit

![Circuit fritzed](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/CircuitBoard.png)
*<p style="text-align: center;">Fig.15. Circuit for this tutorial.</p>*

The blue cables is the data cables, red is 3v3 and black is GND, the LoRaWAN will have one black, red, yellow and white cable, these should be connected as shown in the circuit diagram.

Notice that the DH11 is a four pin in the diagram, ignore this as the one linked in this tutorial is a three pin. But the most important is to always check the hardware you buy so that the circuit is changed depending if the hardware is the same or not.

None of the connected hardware is in need of any resistors. 

As the DH11 is a serial input we need to use one of the UART pins. Therefore the GP13 was selected for this hardware. The Photoresistor on the other hand is an analog input, which is the ADC tag in the Pico layout. For our circuit we used GP27.

Note that The photoresistor in the picture fig.15 is not the one used in the project but the connections are as the circuit shows.

## Platform

For this project I wanted to learn LorAWAN and ended up using [Helium](https://www.helium.com/) as the selected platform as it was the only LoRaWAN network that I could easily connect to from home. Together with Helium I am also using Datacake to store and visualize the data. Datacake also sends me an email if I should roll up the blinds or roll them down. So Helium receives the data that the Pico collects, then retransmits it to Datacake that then stores it and visualize it.

## The code

**Note:** The code is stored on my [github](https://github.com/Erikborgis/IoT-Project) and can be seen there.

There is 4 files:
* main
* lightsensor
* temphumid
* loraWan

I opted out of the boot file as I did not feel the need for it.

```python
import binascii
import struct
import temphumid
import lightsensor
from machine import Pin, ADC
import time
from loraWan import lora

lora = lora()
pinTempHumid = Pin(13)
pinLightSensor = Pin(27)
ldr = ADC(pinLightSensor)
led = Pin("LED", Pin.OUT)
```
In the main file I start with importing all the needed libraries, I then go ahead and setup the different pins that will be used.

```python
lora.configure(DEV_EUI, APP_EUI, APP_KEY)

lora.startJoin()
print("Start Join.....")
while not lora.checkJoinStatus():
  print("Joining....")
  time.sleep(1)
print("Join success!")
led.on()
```

The program then goes on tries to join a Helium network. When and if it succeed to join the LED on the Pico will turn on to notify that joining has been successful. 

```python
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
```

Ones the program has successfully joined a network, the Pico will continue collecting the data.
I then use an if statement to decide if the blinds should be up or down, this is a combination of how bright it is and how warm it is inside of the room, these numbers can of course be calibrated for personal preferences. Here we also makes the data into integers instead of floats as we want to send as small data as possible.

Ones the data has been collected the Pico continues to pack it into a package. As the only value being able to be negative is the temperature_int this is the only one we send as an H(unsigned short integer). The humidity and darkness we send as h(signed short integer) meaning it cant be negative there is also a check in the program that makes sure these wont be negative.

When the package has been sent and a response has been received, the Pico then sleeps for 60min before it reruns everything again.

## Transmitting the data

As I wanted to learn as much as possible, I am using the LoRa even though it will for this project only be staying inside the apartment. The LoRa is however more battery efficient than Wi-fi so there is that benefit. The only LoRa network available to me from my apartment was Helium, so I went for that.

LoRa (Long Range) is a low-power, wide-area networking technology designed for long-range communication with low data rates. It operates in the unlicensed ISM (Industrial, Scientific, and Medical) bands, providing long-range connectivity while consuming minimal power.

I send data every hour, to minimize battery consumption and data charges. For a project with the designed goal like this there is no need to send data more often than that either. So each hour was something I thought would be enough. For the future however it could be made so that it doesn't check during the nights as there is no need rolling the blinds down at that point of time.

```python
  payload = struct.pack(">hHHb", temperature_int, humidity_int, darkness_int, blindState)
  payload = binascii.hexlify(payload).decode("utf-8")

  lora.sendMsg(payload)
  print("Sent message:", payload)

  response = lora.receiveMsg()

  if response != "":
    print("Received: ", end=": ")
    print(response) 
```

The data is being packaged here and sent, we are also trying to receive the acknowledgment/reply if it is more than an acknowledgment it would be printed to the terminal.

## Presenting the data

The presentation is done in Datacake as it seemed like a simple widget to use, which it surely was. It made it really easy for the integration from Helium. As I opted for the free version I am allowed to send 500 datapoints/day and retain data for 7 days. And that is definitely enough for a project of this size. As I will only send 4 different values each hour I wont be close to the limit of 500.

It was fairly easy to create rules in Datacake as well, so creating an email service was not so hard. Datacake will send me an email once an hour reminding me if I need to pull up or down the blinds, seeing as it is not automated yet.

![Email From Datacake](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/Email.png)
*<p style="text-align: center;">Fig.16. Email from Datacake.</p>*

![Datacake Dashboard](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/Dashboard.png)
*<p style="text-align: center;">Fig.17. Dashboard on Datacake.</p>*
  
![Datacake Dashboard](https://hackmd.io/_uploads/BywsvFeF2.png)
*<p style="text-align: center;">Fig.18. Dashboard blinds up on Datacake.</p>*

So on the dashboard the last reading of the temperature is shown in the top left, just to the right of it we have the state of the blinds, in the future this will state if they have been rolled down or not by the software. We then have the temperature history, using this we may see if the temperature actually declines when the blinds are down. As of writing this report, they are pulled down. Just below that we have the humidity to the left and the amount of darkness, the lower the Darkness is the brighter it is. And the reason it is still bright is due to it standing behind the blinds.

## Finalizing the design

![My connections](https://github.com/Erikborgis/IoT-Project/blob/main/Pictures/MyLayout.png)
*<p style="text-align: center;">Fig.18. My connections.</p>*

---

In conclusion to this tutorial, I have created an IoT application that will use temperature and light data to be able to recommend if blinds should be down or up to get a better inside environment. I would however have wanted to actually make the blinds be automated, but as I haven't found an existing motor or blinds in a fair pricerange I haven't gotten to it. 
At the moment it is connected to a wall socket, I would like to connect it to a battery in the future and also 3D print a nice case, as, to be honest... I am not really allowed to keep it as visible in the living room as I would like at the moment.

Overall I am really happy with my project even though there is a ton of improvements to be made, but who said that Rome was built in a day?

I have learned a lot from this course and looking forward to keep on learning by myself now when I have the basic of it.













