myuniquelist=[]
myleftovers=[]

def add(num):
    lnum =len(myuniquelist)
    if lnum <1:
        myuniquelist.append(num)
        return 1
    else:
        for i in range(lnum): 
            if num == myuniquelist[i]:
                myleftovers.append(num)
                return 0               
    myuniquelist.append(num)
    return 1
    
print(len(myuniquelist))    
test1=9
print(bool(add(test1)))

print(len(myuniquelist))      
test2=3
print(bool(add(test2)))

print(len(myuniquelist))  
test3=9
print(bool(add(test3)))

hot= int(input("Please Input a number?\n"))
result= add(hot)
print("The Number inputed was ", bool(result))
print("This is the Unique List ",myuniquelist)
print("This is the Leftover List ",myleftovers)
    