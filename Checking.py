
lst1 = [10,50,80,90,45,70]
lst2 = [80,125,100,112,115]
lst3 = []
lst4 = []


def find(value,lst1):
    for a in lst1:
        if(a==value):
            return True
    return False
# the function check takes two arguments lst1 and lst2
# lst1 and lst2 contains a list of integers 
# for every integer in lst1, function should add all other values
#present in the respective other indexes in the same lst1

#for every integer in lst1, add all other values in lst1 and find if that sum
#exists in lst2
# 
# goal is to find if the sum of each pair in list1 exists in list2 
#  
def check(lst1,lst2):
    for i in lst1:
        for j in lst1:
            y = i + j
            for a in lst2:
                if (a == y):
                    print("match")
                    lst3.append(i)
                    lst4.append(j)
              
    

    
    return


def check1(lst1,lst2):
    # this will track first for loop for i
    a = -1
    # this will track second for loop for j
    b = -1
    for i in lst1:
        # i and j shouldn't take values present at the same index
        a = a + 1
        for j in lst1:
            b = b + 1
            if ( b > a):
                # since both indexes are not same we will get into below code
                if(find(i+j,lst2)):
                    if(False == find(i+j,lst3)):
                        lst3.append(i+j)
        b = -1

check1(lst1,lst2)
#check(lst1,lst2)
print(lst3)