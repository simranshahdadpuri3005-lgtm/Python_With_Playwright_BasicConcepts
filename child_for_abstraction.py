from Abstraction import abstraction_Method

#we cannot create object of abstract class and hence we have to inherit it and them create the objects
class child_for_abstraction(abstraction_Method):
    def click(self): #redeclaring the function with body here
        print ("i am an abstract click method")  #implement the abstract function declared in another class

    def get(self):
        print ("i am an abstract get method")

obj1 = child_for_abstraction()
obj1.click()
obj1.get()
