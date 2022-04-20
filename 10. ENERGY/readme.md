# ENERGY #
## Introduction ## 

Before using batteries with LopY, it is necessary to show how the microcontroller works with both memories (Flash and RAM) to understand sleep modes. Inside each microcontroller, they have different registers (memory arrays) to store relevant information temporarily. One of these is the program counter register which holds the compiled current instruction to inform the memory of the next instruction to read. When one instruction is taken to be executed, flash memory, with help from other registers, sends the information to Arithmetic Logic Unit (ALU) and RAM to process it. Then, Flash memory uses the program counter register to know the next instruction to be compiled.

![PYCOM](https://github.com/puldavid87/PYCOM/blob/main/10.%20ENERGY/e1.png)

## SLEEP ##
There are several methods to make your device sleep.
[Pycom docs](https://docs.pycom.io/tutorials/basic/sleep/)
### time.sleep() ##

This instruction freezes (block the program counter) memory *t* time. Therefore the system does not save energy. 

``` python
import time

time.sleep(1) #sleep 1 second

time.sleep_ms(10) #sleep 10 milliseconds

time.sleep_us(10) #sleep 10 microseconds

```
This instruction 

### machine.sleep() ### 
command will put the controller into a light sleep mode. WiFi and BLE are switched off, but the main CPU and RAM are still running. the LoRa, SigFox and LTE modems are stopped as well and have to be re-initialized after wakeup. The controller will continue running the code after waking up. It reduces the RAM consumption.

``` python
import machine
machine.sleep(1000*t, False) # t-> time in seconds to seelp
```
**Setting the second argument to True will restore the WiFi and BLE after wakeup.**

### machine.deepsleep() ###
Deepsleep disables, next to the lightsleep, the main CPU and RAM. This leaves only a low power coprocessor and RTC timer running. After waking up, the board will start again at boot.py, just like with pressing the reset button. Restart memories and program counter.

``` python
import machine
machine.deepsleep(1000*t, False) # t-> time in seconds to seelp, also you can use without time.
```
**Using deepsleep() will also stop the USB connection. Be wary of that when trying to upload new code to the device!. If you are testing this mode, be sure to use *t* for at least 30 seconds to update the firmware without issues.** 

Sometimes, we want to know the reason the board woke up, to differentiate the difference between pressing the reset button and waking up from sleep. We can also determine the time left on the sleep timer.

``` python
wake_pins = [Pin('P10', mode=Pin.IN, pull=Pin.PULL_DOWN)]
machine.pin_sleep_wakeup(wake_pins, machine.WAKEUP_ANY_HIGH, True)
```

**be careful with the PULL_DOWN AND WAKE UP ANY HIGH, sometimes people use PULL UP and WAKEUP_ANY_HIGH and the system restarts constantly, Do you know why?**

### time.ticks() ### 
You can know how long each instruction takes to the memory process it
``` python
import time
machinestarts=time.ticks_ms()
instructions
machinefinishes=time.ticks_ms()-machinestarts
```
## Reading battery voltage ##
Each shield allows you to read the battery voltage, though in a slightly different way.
``` python
from machine import ADC
adc = ADC()
bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P16')
vbat = bat_voltage.voltage()
# note that the expansionboard 2.0 has a voltage divider of 115K / 56K to account for
print('battery voltage:', vbat*1.5, 'mV')
```
## Assignments ## 
* Test each example with the CO2 sensor to check how sleep modes and reading the battery voltage work.
* Can you determine how long the WiFi/Lora communication and the sensor take to be stable?
* What is the minimum time in light sleep to get stable sensor reading? Do you send the first sensor lecture to the cloud?
* What is the minimum time in light sleep to get stable sensor reading?
* Compare the sensor readings when the system goes to sleep and when it is not. Do you notice any change?

