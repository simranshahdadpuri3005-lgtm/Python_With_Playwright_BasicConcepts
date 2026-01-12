from Class_For_Declarations import FirstClass

#we need to create the object to call / use the functions of FirstClass class declared in Class_For_Declarations python file

firstObject = FirstClass()
firstObject.func1("called in second class using firstobject")

secondObject = FirstClass()
secondObject.S1 ="updated constructor  or instant variable"  #we are overriding the value of S1 declared in Class_For_Declarations.py file
secondObject.func1("called in second class using secondObject")

#data updated in one object does not impact data in another obeject of the same class

print("Firstobject S1 variable is", firstObject.S1)
print("SecondObject S1 variable is", secondObject.S1)
print("Firstobject S1 variable is", firstObject.S1)

#we can call the class or static variables using classname or class objects.

print("before update firstclass variable s is", FirstClass.s)
print("before update firstobject variable s is", firstObject.s)

FirstClass.s ="updated the s static variable of firstclass"

print("after update firstclass variable s is", FirstClass.s)
print("after update firstobject variable s is", firstObject.s)