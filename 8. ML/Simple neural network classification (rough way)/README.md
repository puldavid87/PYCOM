
# Deep Learning Binary Classifier #

## Introduction ##

Machine learning algorithms can describe phenomena or human behavior through complex mathematical functions. Therefore, they need high computational resources. However, tinyML is designed to run on small devices to improve the making decision process inside of it. Consequently, the classification algorithms learn from past experiences 
(training set) to assign new instances a pre-defined group (label). 

## Step 1: Data acquisition ##

### System descryption: ###

The electronic system proposed is to detect if the SCD30 (CO2, temperature, and humidity) sensor has been tampered with by people blowing on him. Therefore, the electronic system can detect two labels: adequate environmental data and tampered data. The code is developed in Python. 

### Assembling the training and test set ###
 The electronic system takes samples every 5 seconds for three variables sending them by Serial communication to a server/desktop to store them. As a result, the dataset has 400 samples for label 1 (sensor is working normally) and 200 samples for label 2 (you have to blow over the sensor). The dataset can be download here: [link](https://github.com/puldavid87/PYCOM/blob/main/8.%20ML/Simple%20neural%20network%20classification%20(rough%20way)/data.csv).
 
 To receive the data and store them from the computer, the Python code is:
 ``` python
#Libraries:

import pandas as pd
import serial 
#create the dataframe
dataset=pd.DataFrame(columns=["co2","temp","hum"])
# serial communication object
com=serial.Serial(port='COM12', baudrate=115200)
#confirmation variable
i=0
while True:
#waits to incoming data
    if(com.in_waiting > 0):
     # variabe recives data
        datos=com.readline()
        # variable divides the data by separator ";"
        val=datos.split()
        # confirmation the data separation
        if len(val)>4:
        #400 samples, you can change the number for samples.
            if i<400:
                # store data in the dataframe
                dataset=dataset.append({'co2' : val[0].decode("utf-8") , 
                                        'temp' : val[2].decode("utf-8") ,
                                        'hum' : val[4].decode("utf-8") },
                                        ignore_index=True)
                #confirmation
                i+=1
                print(i)
            else:
               # close the COM port.
                com.close()
#export to csv the model
dataset.to_csv("data1.csv")
 ```
The code in the electronic device is:

``` python
import time
import math
import pycom
from machine import UART                    
from machine import I2C
from scd30 import *
uart = UART(0, baudrate=115200)             # UART configuration
pycom.heartbeat(False)  # disable the heartbeat LED
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
# Yay for libraries!
sensor = SCD30(i2c, 0x61)
while True:
    for i in range (500):
         # Wait for sensor data to be ready to read (by default every 2 seconds)
        if sensor.get_status_ready() != 1:
            time.sleep_ms(200)
        (co2, temperature, hum) = sensor.read_measurement()
            # Adjust for PCB heating effect. 
        temperature -= 3 # NOTE: Found this value somewhere online
        #send the information
        print(round(co2,2),';',round(temperature,2),';',round(hum,2))
        time.sleep_ms(5000)
```

## Step 2: Model construction ##

### Split the data set in training and test set ###

``` python
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dataset=pd.read_csv('data.csv', sep=';')
X= dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#encode the label and scale the training set
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y)
sc=MinMaxScaler()
X=sc.fit_transform(X)
X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=0)


#Figure because we can :)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_train[:,0],X_train[:,1],X_train[:,2],c=y_train+1)
ax.set_xlabel("CO2")
ax.set_ylabel("Temperature")
ax.set_zlabel("HUmidity")
plt.show()
```
![Figure](https://github.com/puldavid87/PYCOM/blob/main/8.%20ML/Simple%20Classifier/fig.png)

### Classification model ### 

To see and understand better, you can check this: [Neural Network](https://keras.io/).

### NN model ###
``` python
#Neural network model 
# The main idea is train a model with less layers and neurons.
#star the model
model = Sequential()
#NN architecture
#input_shape=(3,) -> variables or sensor as input
model.add(Dense(3, input_shape=(3,), activation='relu', name='fc1'))
model.add(Dense(3, activation='relu', name='fc2'))
#binary classification just one layer
model.add(Dense(1, activation='sigmoid', name='output'))
#compile the model
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
#train de model
history=model.fit(X_train, y_train, verbose=1, validation_split=0.1, epochs=50)

#Graphical summary
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.ylabel('ACCURACY',fontname="Times New Roman")
plt.xlabel('EPOCH',fontname="Times New Roman")
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.ylabel('LOSS',fontname="Times New Roman")
plt.xlabel('EPOCH',fontname="Times New Roman")
plt.legend(['train', 'validation'], loc='upper left')
plt.show()
```
###  Model test ###

``` python
# evaluamos el modelo
scores = model.evaluate(X_test, y_test)


from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report 
y_pred=model.predict(X_test).round()
#
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test,y_pred))
```
## Step 3: Export the inference ## 

### Layers and neurons ###
Thanks to: (Jeff Heaton ) [https://github.com/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class_03_5_weights.ipynb]
``` python
#exporting the model
# Dump weights
for layerNum, layer in enumerate(model.layers):
    weights = layer.get_weights()[0]
    biases = layer.get_weights()[1]
    
    for toNeuronNum, bias in enumerate(biases):
        print(f'{layerNum}B -> L{layerNum+1}N{toNeuronNum}: {bias}')
    
    for fromNeuronNum, wgt in enumerate(weights):
        for toNeuronNum, wgt2 in enumerate(wgt):
            print(f'L{layerNum}N{fromNeuronNum} \
                  -> L{layerNum+1}N{toNeuronNum} = {wgt2}')

```

### Export layers and neurons

Output from spyder call 'get_namespace_view':
0B -> L1N0: 0.0
0B -> L1N1: -0.046640533953905106
0B -> L1N2: -0.008210621774196625
L0N0                   -> L1N0 = -0.40018725395202637
L0N0                   -> L1N1 = -0.20207683742046356
L0N0                   -> L1N2 = -0.8088093996047974
L0N1                   -> L1N0 = -0.45806193351745605
L0N1                   -> L1N1 = 0.6922328472137451
L0N1                   -> L1N2 = 0.04006657004356384
L0N2                   -> L1N0 = -0.5675060749053955
L0N2                   -> L1N1 = 1.4084460735321045
L0N2                   -> L1N2 = -0.8523695468902588
1B -> L2N0: -0.011691042222082615
1B -> L2N1: 1.0252364873886108
1B -> L2N2: 0.0
L1N0                   -> L2N0 = 0.11224651336669922
L1N0                   -> L2N1 = 0.3702874183654785
L1N0                   -> L2N2 = 0.001936197280883789
L1N1                   -> L2N0 = 1.5117204189300537
L1N1                   -> L2N1 = -0.41452986001968384
L1N1                   -> L2N2 = -0.07663965225219727
L1N2                   -> L2N0 = -0.3833346366882324
L1N2                   -> L2N1 = -0.2300751656293869
L1N2                   -> L2N2 = -0.956559419631958
2B -> L3N0: -0.5874778032302856
L2N0                   -> L3N0 = 1.582396149635315
L2N1                   -> L3N0 = -0.8516733646392822
L2N2                   -> L3N0 = -0.6935510635375977

## Step 4: Real tests ## 

The model can be exported in an external file .py to call it in the main function to run it in the electronic device.

``` python
#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: project -> Binary classification algorithm
# IoT course
#
#https://forum.micropython.org/viewtopic.php?t=1747
# Thanks Niels..!!
#

import time
import math
import pycom
import gc
from machine import UART                    
from machine import I2C
from scd30 import *
uart = UART(0, baudrate=115200)             # UART configuration
pycom.heartbeat(False)  # disable the heartbeat LED
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
# Yay for libraries!
sensor = SCD30(i2c, 0x61)
y_pred=0

def sigmoid_fuction (input):
    e=2.71828
    return (1/(1+pow(e,-input)))

def neuralmodel (input):
    l0n0=(input[0]-1201.52)/(40000.0-1201.52)
    l0n1=(input[1]-22.19)/(32.04-22.19)
    l0n2=(input[2]-27.9)/(93.81-27.9)
    l1n0=max(0,((l0n0*-0.40)+(l0n1*-0.45)+(l0n2*-0.56)))
    l1n1=max(0,((l0n0*-0.20)+(l0n1*0.69)+(l0n2*1.41)) - 0.047)
    l1n2=max(0,((l0n0*-0.81)+(l0n1*0.04)+(l0n2*-0.85))-0.008)

    l2n0= max(0,((l1n0*0.11)+(l1n1*1.51)+(l1n2*-0.38))-0.011)
    l2n1= max(0,((l1n0*0.37)+(l1n1*-0.41)+(l1n2*-0.23))+1.025)
    l2n2=max(0,((l1n0*0.002)+(l1n1*-0.08)+(l1n2*-0.95)))

    l3n0=sigmoid_fuction(((l2n0*1.58)+(l2n1*-0.85)+(l2n2*-0.69))-0.5874)
    if l3n0 < 0.5:
        return 0
    else:
        return 1


while True:
    for i in range (500):
         # Wait for sensor data to be ready to read (by default every 2 seconds)
        if sensor.get_status_ready() != 1:
            time.sleep_ms(200)
        (co2, temperature, hum) = sensor.read_measurement()
            # Adjust for PCB heating effect. 
        temperature -= 3 # NOTE: Found this value somewhere online

        if co2 > 0 and temperature > 0 and hum > 0:
            data=[co2,temperature,hum] # put in array the sensor data
            #make the prediction
            y_pred=neuralmodel(data)
            #send the information and the label
            print(round(co2,2),';',round(temperature,2),';',round(hum,2),';',y_pred)
        else :
             print(round(co2,2),';',round(temperature,2),';',round(hum,2))
        time.sleep_ms(4000)
        gc.collect()
        print(gc.mem_free())

        
```
