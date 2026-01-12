#there are 3 types of access modifiers : public, private and protected
#for private we have to give __varname ; private var or functions cannot be accessed outside the class in which they are defined
#for protected, we have to _varname ; it works same to public and has no restrictions like private; its just an indication to not use it
#encapsulation is the process of binding variables and functions inside a class and controlling access to them

from Class_For_Declarations import FirstClass

obj = FirstClass()
print(obj.S1)

print(obj._b)

#this will give the error because we cannot access private variables outside the original class; hence commented it
#print(obj.__a) 

#this will give the error because we cannot access private functions outside the original class; hence commented it

# obj1 = FirstClass()
# obj1.__func4("Inside fucntion 4 for child class")
