# fuction structure
# def-> definition
# fuction_1 -> name's fuction
# () -> input parameters (none)
import time

def fuction_1():
    #first fuction
    print("I'm the first fuction :)")
    time.sleep_ms(500)

#(limit) -> input fuction parameter 
def fuction_2(limit):
     for i in range(limit):
         print("Second fuction counting:",i)
         time.sleep_ms(100)

def fuction_3(data):
    output=list()
    for i in data:
        aux=i.upper()
        if aux == 'A' or aux == 'E' or aux == 'I' or aux == 'O' or aux == 'U':
            output.append('*')
        else:
            output.append(aux)
    return output


