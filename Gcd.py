import random #imports random function
import time   #imports time function

# this is iterative version of GCD
def computeHCF(x,y):                                #defined new hcf function
      if x > y:                                     #checks whether x > y
        smaller = y                                 # if x is greater assigns smaller = y
      else:
          smaller = x                               # if is x is smaller then samller = x
      for i in range(1,smaller+1):                  # iterates in range(1,smaller+1)
          if((x % i ==0) and (y % i ==0)):          # checks whether x and y divisible by i
               hcf = i                              # i value is stored in hcf
               
      return hcf                                    # returns hcf


# this is recurssive version of GCD
def gcd(num1,num2):                                 # new gcd function
    if(num2==0):                                    # checks whether num2 == 0
        return num1                                 # if num2 = 0 then returns num1
    else:                                           
        return gcd(num2,num1%num2)                  #returns gcd(num2,num1%num2)


# This is better iterative version GCD
def iterative_gcd(a,b):                             # defined new iterative function
    if (b == 0):                                    # checks if b == 0 
        return a                                    # if b==0 returns a 
    while True:                                     # starting the loop
        z = a                                       # a value is stored in z
        a = b                                       # b vaue is stored in a
        if (a == 0):                                # checks if a ==0 
            break                                   
        b = z % a                                   
    return z


# this is better itertative version_1 of gcd
def iterative1_gcd(a,b):                          # defined new iterative gcd
    while True:                                   # loop starts
        if(b==0):                                 # checks if b == 0
            return a                              # returns a 
        z = a                                     # a value is stored in z
        a = b                                     # b value is stored in a
        b = z % a

# following is the main function
a=[]                                             # creates empty list
b=[]                                             # creates empty list
c=[]                                             # creates empty list
d=[]                                             # creates empty list
e=[]                                             # creates empty list
f=[]                                             # creates empty list

for i in range(100000):                                 # The loops occurs 10 values
         num1 = random.randint(1,1000000)            # num1 is random integer in the range (1,1000000)
         num2 = random.randint(1,1000000)            # num2 is random integer in the range (1,1000000)

         start = time.time()                         # starts time
         r = computeHCF(num1,num2)                   # computed hcf values stored in r
         print("the H. C. F. using iterative", num1,"and",num2,"is",r) #prints hcf off num1 and num2
         end = time.time()                            
         print("time taken by computeHCF function")  # prints time taken to compute hcf function
         print(end - start)                          # prints end - start
         x = end - start                             # stores end - start in x

         start = time.time() 
         i = iterative_gcd(num1,num2)
         print("the H. C. F. of better iterative",num1," and ", num2, "is" ,i)
         print("Time taken to compute better iterative version is")
         end = time.time()
         print(end - start)
         y = end - start

         start = time.time() 
         s = gcd(num1,num2)
         print("the H. C. F. using recurssion", num1,"and",num2,"is",s)
         end = time.time()
         print("Time taken by gcd function")
         print(end - start)
         z = end - start

         a.append(r)      # the values of r is pushed to list a

         b.append(s)      # the values of s is pushed to list b
         c.append(i)      # the values of i is pushed to list c
         d.append(x)      # the values of x is pushed to list d
         e.append(y)      # the values of y is pushed to list e
         f.append(z)      # the values of z is pushed to list f  

print("The iterative version values\t\t\t",a)
print("The better iterative version values\t\t",c)
print("The recursion version values\t\t\t",b)


print("The total time of computehcf is", sum(d))
print("The total time of gcd is", sum(e))
print("The total time of better iterative version is", sum(f))
