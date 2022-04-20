# ENERGY #
## Introduction ## 

Before using batteries with LopY, it is necessary to show how the microcontroller works with both memories (Flash and RAM) to understand sleep modes. Inside each microcontroller, they have different registers (memory arrays) to store relevant information temporarily. One of these is the program counter register which holds the compiled current instruction to inform the memory of the next instruction to read. When one instruction is taken to be executed, flash memory, with help from other registers, sends the information to Arithmetic Logic Unit (ALU) and RAM to process it. Then, Flash memory uses the program counter register to know the next instruction to be compiled.

![PYCOM](https://github.com/puldavid87/PYCOM/blob/main/10.%20ENERGY/e1.png)

## SLEEP ##
There are several methods to make your device sleep.
[Pycom docs](https://docs.pycom.io/tutorials/basic/sleep/)
### time.sleep() ##

This instruction freezes memory *x* time. Therefore the system does not save energy. 

``` python
import time

time.sleep(1) #sleep 1 second

time.sleep_ms(10) #sleep 10 milliseconds

time.sleep_us(10) #sleep 10 microseconds

```
This instruction 

### Light.sleep() ### 
command will put the controller into a light sleep mode. WiFi and BLE are switched off, but the main CPU and RAM are still running. the LoRa, SigFox and LTE modems are stopped as well and have to be re-initialized after wakeup. The controller will continue running the code after waking up.

``` python
machine.sleep(1000*t, False)
```
**Setting the second argument to True will restore the WiFi and BLE after wakeup.**
