import time
import math
from firstlib import fuction_1 
from firstlib import fuction_2
from firstlib import fuction_3 
from secondlib import myclass
mathfuction=myclass(2,1,3)
while True:
    print("First fuction:")
    fuction_1()
    time.sleep_ms(500)
    fuction_2(10)
    time.sleep_ms(500)
    print("Third fuction:")
    data=fuction_3('hello')
    print(data)
    time.sleep_ms(500)
    print("Second library with class")
    out=mathfuction.addition()
    print("addition:", out)
    time.sleep_ms(500)
    out=mathfuction.subtraction()
    print("subtraction:", out)
    time.sleep_ms(500)
    out=mathfuction.pow1()
    print("POW:", out)
    time.sleep_ms(500)


