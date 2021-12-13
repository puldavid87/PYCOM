# Input / Output ports
## Theory:
### Functionality:

Output:

The simple way to understand embedded systems (pycom) is when the system only has two states, true (3.3 volts, HIGH) and false (0 volts, LOW). We can test these states when the system sends or receives them. We can send these states to another electronic part such as leds. To do this, we must select the pin or pins that we will use. Therefore, the figure shows the pin distribution, each pin called GPIO can be used to send or receive logic states. Also, we need to stop the machine for several seconds to see what happens with leds. If we do not stop to machine, the system will run so fast that we can not see if the LEDs are on or off.   

Input: 

Sometimes it is necessary to acquire data from electronic devices. In this case, the most simple of them are buttons or switches. To connect them, we have to be sure that the system receives the logic state without errors. We can use a pull-down or pull connection ( [More information](https://www.electronics-tutorials.ws/logic/pull-up-resistor.html)). Then, we need to compare to know if the state of the pin has been changed. Next, we can receive data from switches. However, to use buttons, it is necessary to stop the machine to avoid rebounds. That means when people press the button; they do so slow compared to the machine, which reads this action many times, and at the point of the press there can be uncertainty of the value s.t. it can go back and forth from one read to the next. You can see it in ( [Code: io4.py](https://github.com/puldavid87/PYCOM/blob/main/2.%20%20IO%20ports/io4.py))


PinOut:

![Esta es una imagen](https://github.com/puldavid87/PYCOM/blob/main/fipy-pinout.png)

### Libraries:
```
from machine import Pin
import time
```
### Code Structures:
```
variable= Pin('PIN', mode=Pin.MODE)                 variable.value(x)                     time.sleep(s)
PIN-> selected pin (P8,P9)                             x-> 1: HIGH                          s-> stopping the machine in seconds
       MODE-> OUT                                      0: LOW                               time.sleep_ms(ms) 
              IN                                                                                    ms -> stopping the machine in miliseconds
```
## Examples:
```
io1.py -> Simple Output ports configuration (Hello World..!!)
io2.py -> For and If cycles with output ports configuration
io3.py -> Simple Input configuration
io4.py -> button configuration avoiding rebounds
```
