# Few String Functions

#strings are immutable

S= "hello how are you all"

print(len(S))  # Total characters including spaces

print(len(S.replace(" ", ""))) #Count characters without spaces

print(len(S.split())) #Count words

# replace spaces with some other character
S2= "hello how are you all"
print(S2)
S3 = S2.replace(" ", "|")
print(S3)

print(S.upper())  #convert string chracters to uppercase

print(S.lower())  #convert string chracters to lowercase

print(S.capitalize())  #convert only first letter of the sentence to uppercase

print(S.title())  #convert first letter of every word in the sentence to uppercase

print(S.replace('h','z'))  #replace all h in the setnce to z

print(S[-1])  # Last 1 character

# Slicing format is: string[start:end]
# Python slices left to right

print(S[0:4])  #slicing of string, first 4 characters

print(S[:4])  #slicing of string, first 4 characters

print(S[-7:])  #slicing of string, from the end, last 7 characters

print(S.split()[-1])  # Last word	

print(S[::1]) #print the string with step=1

print(S[::-1])  # reverse a string[::-1] means start to end, step = -1 (reverse)

#another way of reversing string using for loop
S5 ="Hellow world"
reverseString =""

for i in S5:
    print("i holds the value as ",i)
    reverseString =  i+reverseString
    print("now i is ",i)
    print("now reverseString is ",reverseString)

print("final reverString is", reverseString)


#Use strip to remove before and after the end of words

S1= "        hello how are you all     "
print(S1) 
print(len(S1))

S4 = S1.strip()
print(S4) 
print(len(S4))

S2 = S1.rstrip()  # remove spaces only from right side
print(S2) 
print(len(S2))

S3 = S1.lstrip() # remove spaces only from left side
print(S3) 
print(len(S3))


#convert a string into a list
S1= "hello how are you all"
S2 = S1.split(" ")
print(S2)

S3 = ("").join(S2)
print(S3)

list1 = ["automation", "testing"]
S4 = ("|").join(list1)
print(S4)

print(S4.count("a")) # count the number of a in the string s4




Frozenset1 = frozenset([1,2,3,1])
print(Frozenset1)  #frozenset cannot be updated and does not allow duplicate values


