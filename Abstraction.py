#abstraction is process of hiding the implementation and using the methods
#abc is the python library

from abc import ABC, abstractmethod

class abstraction_Method(ABC):
    
    @abstractmethod   #this is a decorator
    def click(self):  #declare the function with out the body or the impementation
        pass

    @abstractmethod
    def get(self):
        pass

    def abc_function2(self):
        print("printing abstract function")