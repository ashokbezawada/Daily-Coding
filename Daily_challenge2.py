#code which returns the next number
def addition(x):
    x = x + 1
    return x
x = int(input("Enter the number to be incremented"))
y = addition(x)
print("the number incremented is", y)


#Program to find area of triangle
def areaoftriangle(base,height):
    area = base*height/2
    return area
base = int(input("Enter the base of a triangle"))
height = int(input("Enter the height of a triangle"))
a = areaoftriangle(base,height)
print("The area of triangle is \t", a)


#Return the reaminder of two numbers
def remainder(d,e):
    if (e == 0):
        print("enter a number greater than zero")
    else:
        z = d % e
        return z
d = int(input("enter the number"))
e = int(input("enter the number"))
f = remainder(d,e)
print("The remainder of two numbers is \t",f) 

#return the first element of a list
num_list = [1,2,3,4]
def first_value(num_list):
   
    return num_list[0]

print("The first element in the list /t", num_list[0])


#Hours and minutes to seconds
def convert(n,m):
    seconds = (n*60)*60 + (m*60)
    return seconds

n = int(input("enter the no.of hours"))
m = int(input("enter the no.of minutes"))
i = convert(n,m)
print("The total no.of seconds is ",i)  