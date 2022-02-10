class myclass:
    #init fuction
    #All classes have a function called __init__(), which is always executed when the class is being initiated.
    #Use the __init__() function to assign values to object properties
    def __init__(self,number1,number2,number):
        self.number1=number1 #-> self.number1 we can use en each class fuction 
        self.number2=number2
        self.number=number

    def sum (self):
        return self.number1+self.number2
    
    def subtraction(self):
        return self.number1-self.number2
    
    def addition (self):
        return self.number1*self.number2
    def pow1(self):
        result=1
        for i in range(self.number):
            result=result*self.addition()
        return result