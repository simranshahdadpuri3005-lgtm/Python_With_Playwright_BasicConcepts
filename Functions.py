#user defined functions

#function names cannot have spaces special characters

# example of non-parameterized function
def replacingSpaces():
    S= "hello how is the weather today"
    S1 = S.replace(" ", "||")
    print(S1)

replacingSpaces() #function should be called to function to be executed


# example of parameterized function
S= "hello how are you all"
S2= "another string"
S3= "one more string"

def replacingSpaces1(stringValue):
    S4 = stringValue.replace(" ", "|")
    print(S4)


replacingSpaces1(S)
replacingSpaces1(S2)
replacingSpaces1(S3)

# example of 2 parameters
S= "hello how are you all"
S2= "another string"
S3= "one more string"

def two_params(a,b):
    print("first pramam is", a)
    print("second pram is", b)


two_params(S,S2)
two_params(S3,S)

def sum(a,b):
    c=a+b
    print(c)

sum(4,7)

def sum1(a,b):
    c=a+b
    return c

value = sum1(2,7)
print("sum total is", value)    



