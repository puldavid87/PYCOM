# PYCOM
Software development for pycom platform
## BASIC:
Documentation: 
[Pycom documentation](https://docs-mk2.readthedocs.io/en/latest/)
[Pycom docs](https://alepycom.gitbooks.io/pycom-docs/content/)

### PinOut Guide:

![PYCOM](https://github.com/puldavid87/PYCOM/blob/main/fipy-pinout.png)

### Chapter 1: Getting started
Commands
```
Connect (ctrl-shift-c) : Connects to the board
Disconnect : Disconnects from the board
Global settings (ctrl-shift-g) : Opens the installation-wide settings file
Project settings : Opens project specific settings that overwrite global settings
Run (ctrl-shift-r) : Runs currently open file on the board ()
Run selection (ctrl-shift-enter) : Rns the current selected line on the board
Sync (ctrl-shift-s) : Synchronizes the complete project to the board, using the sync folder settings
List serial ports : Lists all available serial ports and copies the first one to the clipboard
Get firmware version : Displays firmware version of the connected board
Get WiFi SSID : Gets the SSID of the boards WiFi access point
Help : Print this list of commands and settings
```

Useful keymaps:
```
ctrl-shift-c : (Re)connect
ctrl-shift-g : Global settings
ctrl-shift-s : Synchronize project
ctrl-shift-r : Run current file
ctrl-shift-enter : Run current Line
```
#### Software Installation

Pymark in Visual Studio Code:
[Instructions](https://docs.pycom.io/gettingstarted/)

#### Pycom Port connection


Windows environment:
```
Device manager-> Ports (COM and LPT)
Determine the COM port used by pycom
```


Once Pymark is installed in Visual Studio Code:
```
Extension -> pycom -> Global settings (ctrl+shift+g)
```
Edit the file:
``` python

{
	"address": "COM12",
	"username": "micro",
	"password": "python",
	"sync_folder": "",
	"open_on_start": true,
	"safe_boot_on_upload": false,
	"py_ignore": [
		"pymakr.conf",
		".vscode",
		".gitignore",
		".git",
		"project.pymakr",
		"env",
		"venv"
	],
	"fast_upload": false,
	"sync_file_types": "py,txt,log,json,xml,html,js,css,mpy",
	"ctrl_c_on_connect": false,
	"sync_all_file_types": false,
	"auto_connect": false,
	"autoconnect_comport_manufacturers": [
		"Pycom",
		"Pycom Ltd.",
		"FTDI",
		"Microsoft",
		"Microchip Technology, Inc."
	]
}
```

Connect the board:
```
ctrl-shift-c
```
Run the example code:
``` python
from machine import Pin
import time
led = Pin('P9', mode=Pin.OUT)

while True:
    print("high")
    led.value(1)
    time.sleep(1)
    print("low")
    led.value(0)
    time.sleep(1)
```

### Chapter 2: Input/Output ports
#### Theory:
##### Functionality:

Output:

The simple way to understand embedded systems (pycom) is when the system only has two states, true (3.3 volts, HIGH) and false (0 volts, LOW). We can test these states when the system sends or receives them. We can send these states to another electronic part such as leds. To do this, we must select the pin or pins that we will use. Therefore, the figure shows the pin distribution, each pin called GPIO can be used to send or receive logic states. Also, we need to stop the machine for several seconds to see what happens with leds. If we do not stop to machine, the system will run so fast that we can not see if the LEDs are on or off.   

Input: 

Sometimes it is necessary to acquire data from electronic devices. In this case, the most simple of them are buttons or switches. To connect them, we have to be sure that the system receives the logic state without errors. We can use a pull-down or pull connection ( [More information](https://www.electronics-tutorials.ws/logic/pull-up-resistor.html)). Then, we need to compare to know if the state of the pin has been changed. Next, we can receive data from switches. However, to use buttons, it is necessary to stop the machine to avoid rebounds. That means when people press the button; they do so slow compared to the machine, which reads this action many times. You can see it in ( [Code: io4.py](https://github.com/puldavid87/PYCOM/blob/main/2.%20%20IO%20ports/io4.py))


PinOut:

![Esta es una imagen](https://github.com/puldavid87/PYCOM/blob/main/fipy-pinout.png)

#### Libraries:
```
from machine import Pin
import time
```
#### Code Structures:
```
variable= Pin('PIN', mode=Pin.MODE)                 variable.value(x)                     time.sleep(s)
PIN-> selected pin (P8,P9)                             x-> 1: HIGH                          s-> stopping the machine in seconds
       MODE-> OUT                                      0: LOW                               time.sleep_ms(ms) 
              IN                                                                                    ms -> stopping the machine in miliseconds
```
#### Examples:
```
io1.py -> Simple Output ports configuration (Hello World..!!)
io2.py -> For and If cycles with output ports configuration
io3.py -> Simple Input configuration
io4.py -> button configuration avoiding rebounds
```
### Chapter 3: Digital Analog Conversion
#### Theory:
##### Functionality:

ADC:

To describe a phenomenon, it is necessary to represent it the most of the cases in voltage. Then, this signal can be scaled to finite numbers called registers. Generally, these registers can be 10,12, and 16 bits.  

DAC: 
Most used in pulse-width modulation. The duty cycle of a periodic signal is the relative width of its positive part about the period. Frequency can be from 125Hz to 20kHz in steps of 122Hz. amplitude is an integer specifying the tone amplitude to write the DAC pin. Amplitude value represents:

0 is 0dBV (~ 3Vpp at 600 Ohm load)

1 is -6dBV (~1.5 Vpp),

2 is -12dBV (~0.8 Vpp)

3 is -18dBV (~0.4 Vpp).

PinOut:
![Esta es una imagen](https://github.com/puldavid87/PYCOM/blob/main/fipy-pinout.png)

#### Libraries:
```
from machine import ADC
import time
```
#### Code Structures:
```
adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16
dac = machine.DAC('P22')        # create a DAC object
dac.write(0.5)                  # set output to 50%
from machine import PWM
pwm = PWM(0, frequency=5000)  # use PWM timer 0, with a frequency of 5KHz
```
#### Examples:
```
adc1.py -> Simple analog digital test
dac1.py -> Simple digital analog test
dac2.py -> PWM
dac3.py -> ADC and DAC configuration
dac4.py -> Input port and PWM configuration

```
### Chapter 4: CX Serial
#### Theory:
Embedded electronics is all about interlinking circuits (processors or other integrated circuits) to create a symbiotic system. In order for those individual circuits to swap their information, they must share a common communication protocol. Hundreds of communication protocols have been defined to achieve this data exchange, and, in general, each can be separated into one of two categories: parallel or serial.

Over the years, dozens of serial protocols have been crafted to meet particular needs of embedded systems. USB (universal serial bus), and Ethernet, are a couple of the more well-known computing serial interfaces. Other very common serial interfaces include SPI, I2C, and the serial standard we're here to talk about today. Each of these serial interfaces can be sorted into one of two groups: synchronous or asynchronous.

A synchronous serial interface always pairs its data line(s) with a clock signal, so all devices on a synchronous serial bus share a common clock. This makes for a more straightforward, often faster serial transfer, but it also requires at least one extra wire between communicating devices. Examples of synchronous interfaces include SPI, and I2C.

Asynchronous means that data is transferred without support from an external clock signal. This transmission method is perfect for minimizing the required wires and I/O pins, but it does mean we need to put some extra effort into reliably transferring and receiving data. The serial protocol we'll be discussing in this tutorial is the most common form of asynchronous transfers. It is so common, in fact, that when most folks say “serial” they’re talking about this protocol (something you’ll probably notice throughout this tutorial) [Sparkfun](https://learn.sparkfun.com/tutorials/serial-communication/all).
#### Functionality:

In this course, serial communication is focused on sending messages to the computer for visualizations interfaces running on local computers.


#### Libraries:
```
from machine import UART #library 
```
#### Code Structures:
```
uart = UART(0, baudrate=115200)        # UART configuration
data=uart.read()        # receive data    print(data)                            # send data
```
#### Examples:
```
cx1.py -> Read/Write chart/strings
cx2.py -> convert string to int serial cx
project -> converting vowels in '*'
```

### Chapter 5: I2C COMMUNICATION
#### Functionality:

In this course, i2c communication is focused on sending messages between sensors and microcontrollers or between only microcontrollers.


#### Libraries:
```
from machine import I2C
```
#### Code Structures:
```
i2c = I2C(2) #
```
#### Examples:
```
cx1.py -> Whitout library
cx2.py -> With librarby: lib folder
```

