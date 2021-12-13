# ANALOG-DIGITAL * DIGITAL-ANALOG CONVERTER
## Theory:

![Megodenas, Public domain, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/5/5a/Conversion_AD_DA.png)

### Functionality:

ADC:

To describe a phenomenon, in most of the cases it is necessary to represent it in voltage, which can be measured. Then, this signal can be scaled to finite numbers called registers. Generally, these registers can be 10,12, and 16 bits, meaning they can represent e.g. $2^{10} = 1024$ different values

DAC: 

![Thewrightstuff, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/b/b8/Duty_Cycle_Examples.png)

Most used in pulse-width modulation. The duty cycle of a periodic signal is the relative width of its positive part about the period. Frequency can be from 125Hz to 20kHz in steps of 122Hz. amplitude is an integer specifying the tone amplitude to write the DAC pin. Amplitude value represents:

0 is 0dBV (~ 3Vpp at 600 Ohm load)

1 is -6dBV (~1.5 Vpp),

2 is -12dBV (~0.8 Vpp)

3 is -18dBV (~0.4 Vpp).

PinOut:
![Esta es una imagen](https://github.com/puldavid87/PYCOM/blob/main/fipy-pinout.png)

### Libraries:
```
from machine import ADC
import time
```
### Code Structures:
```
adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16
dac = machine.DAC('P22')        # create a DAC object
dac.write(0.5)                  # set output to 50%
from machine import PWM
pwm = PWM(0, frequency=5000)  # use PWM timer 0, with a frequency of 5KHz
```
## Examples:
```
adc1.py -> Simple analog digital test
dac1.py -> Simple digital analog test
dac2.py -> PWM
dac3.py -> ADC and DAC configuration
dac4.py -> Input port and PWM configuration

```
