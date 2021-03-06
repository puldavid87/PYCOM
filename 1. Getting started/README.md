# Intrusctions

## Software Installation

Pymark in Visual Studio Code:
[Instructions](https://docs.pycom.io/gettingstarted/)

### Pycom Port connection


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
