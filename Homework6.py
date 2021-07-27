dist={
    "FName" : "Delano",
    "LName" : "Bannister",
    "Age" : 22,
    "DOB" : "March 4, 1998",
    "Nationality" : "Jamaican"
}

def myfirst(a,b):
    if a in dist:
        if b in dist.values():
            return 1
        else:
            return 0
    else:
        return 0
    
#mar= input("Please enter the Key Variable? ")
#mar2= input("Please enter the Value of the Key? ")
mar="FName"
mar2="Delano"
print( "Your Input was ",bool(myfirst(mar,mar2)))