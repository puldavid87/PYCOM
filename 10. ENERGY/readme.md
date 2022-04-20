# ENERGY #
## Introduction ## 

Before using batteries with LopY, it is necessary to show how the microcontroller works with both memories (Flash and RAM) to understand sleep modes. Inside each microcontroller, they have different registers (memory arrays) to store relevant information temporarily. One of these is the program counter register which holds the compiled current instruction to inform the memory of the next instruction to read. When one instruction is taken to be executed, flash memory, with help from other registers, sends the information to Arithmetic Logic Unit (ALU) and RAM to process it. Then, Flash memory uses the program counter register to know the next instruction to be compiled.

![PYCOM](https://github.com/puldavid87/PYCOM/blob/main/fipy-pinout.png)


[Pycom docs](https://alepycom.gitbooks.io/pycom-docs/content/)
