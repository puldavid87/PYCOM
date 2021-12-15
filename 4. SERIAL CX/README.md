# SERIAL COMMUNICATION
## Theory:
Embedded electronics is all about interlinking circuits (processors or other integrated circuits) to create a symbiotic system. In order for those individual circuits to swap their information, they must share a common communication protocol. Hundreds of communication protocols have been defined to achieve this data exchange, and, in general, each can be separated into one of two categories: parallel or serial.

Over the years, dozens of serial protocols have been crafted to meet particular needs of embedded systems. USB (universal serial bus), and Ethernet, are a couple of the more well-known computing serial interfaces. Other very common serial interfaces include SPI, I2C, and the serial standard we're here to talk about today. Each of these serial interfaces can be sorted into one of two groups: synchronous or asynchronous.

A synchronous serial interface always pairs its data line(s) with a clock signal, so all devices on a synchronous serial bus share a common clock. This makes for a more straightforward, often faster serial transfer, but it also requires at least one extra wire between communicating devices. Examples of synchronous interfaces include SPI, and I2C.

Asynchronous means that data is transferred without support from an external clock signal. This transmission method is perfect for minimizing the required wires and I/O pins, but it does mean we need to put some extra effort into reliably transferring and receiving data. The serial protocol we'll be discussing in this tutorial is the most common form of asynchronous transfers. It is so common, in fact, that when most folks say “serial” they’re talking about this protocol (something you’ll probably notice throughout this tutorial) [Sparkfun](https://learn.sparkfun.com/tutorials/serial-communication/all).
### Functionality:

In this course, serial communication is focused on sending messages to the computer for visualizations interfaces running on local computers.


### Libraries:
```python
from machine import UART #library 
```
### Code Structures:
```python
uart = UART(0, baudrate=115200)        # UART configuration
data=uart.read()        # receive data    print(data)                            # send data
```
## Examples:
```
cx1.py -> Read/Write chart/strings
cx2.py -> convert string to int serial cx
project -> converting vowels in '*'
```
