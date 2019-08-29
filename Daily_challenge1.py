#Minutes to Seconds
def convert(minutes):
    return minutes*60
minutes = int(input("enter minutes to convert:"))
y = convert(minutes)
print(y)

#create a function to find maximum edge
def findmax(x,y,z):
    if x > y and x > z:
       print("x is the greatest side")
    if y > x and y > z:
        print("y is the largest side")
    if z > x and z > y:
        print("z is the greatest side") 
x = int(input("enter the side of triangle"))   
y = int(input("enter the side of triangle"))   
z = int(input("enter the side of triangle"))     
f = findmax(x,y,z)
print(f)    

#To find maximum range of a triangle third side
def next_edge(side1, side2):
	nextEdge = ( side1 + side2 ) - 1
	return nextEdge
side1 = int(input("enter the length of side1"))
side2 = int(input("enter length of side2"))
q = next_edge(side1, side2)
print(q)