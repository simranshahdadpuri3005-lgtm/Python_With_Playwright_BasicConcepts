from Class_For_Declarations import FirstClass

class InheritedClass(FirstClass):   #InheritedClass is child of FirstClass
    pass

inhertiedClassObj = InheritedClass()
inhertiedClassObj.func1("inside the clild class using inhertiedClassObj")


#override or polymorphism means multiple functions using same name
class anotherChild(FirstClass):
    def func1(self, a):
        print("function1 is triggered from ", a)

anotherObj = anotherChild()
anotherObj.func1("inside clild class using anotherObj")

class child2(FirstClass):
    def __init__(self):
        super().__init__()   # use super to grab the elements of the parent class also
        self.s2="String in the child class"
        self.s3 ="123"

anotherObj1 = child2()
anotherObj1.func1("inside child2 class obj")


#overloading is same name with different number of paraemeters- it is not present in python
#super keyword acts as binding of parent and child constructor

#overriding is same function name but different definition in parent and child - its present in python
