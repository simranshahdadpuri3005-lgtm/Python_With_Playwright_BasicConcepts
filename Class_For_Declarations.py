
#we are declaring functions in this Class and call its functions in another class
#we need to give a contructor inside a class to use the variables and functions inside the class
#constructor makes sure a separate object is created every time the class functions are called


#there are 3 types of access modifiers : public, private and protected
#for private we have to give __varname ; private var or functions cannot be accessed outside the class in which they are defined
#for protected, we have to _varname ; it works same to public and has no restrictions like private; its just an indication to not use it


class FirstClass:

    s= "Common statement"  #class variable or static variable

    def __init__(self): #__init__ is the constructor
        self.S1 = "S1 is public varaible in parent class" #instant or gloabl or public variable
        self.__a = "a is private variable in parent class"  #private variable
        self._b ="b is the protected variable in parent class"  #protected variable

    def func1(self, a):
        print("My function 1 is triggered from ", a)
        print (self.S1)

    def func2(self, b):
        print("My function 2 is ", b)
        print (self.S1)

    def func3(self, c):
        print("My function 3 is ", c)
        print (self.S1)

    def __func4(self, a):  #func4 is a provate function
        print("My function 4 is triggered from ", a)
        print (self.S1)
        
