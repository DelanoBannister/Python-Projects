import os.path

def check(name):
    if os.path.exists(name+".txt"):
        print ("File exist")
        fileexist(name)
    else:
        print ("File not exist")
        createfile()
        
def createfile():
    name= input("Please Enter the Title of the File you want to Create\n ")
    openfile=open(name+".txt","w+")
    add= input("Please Enter the information you want to put in the File\n")
    openfile.write(add+"\n")
    openfile.close()
    fileexist(name)
    
def update(name):
    present= input("Please Enter the information you want to store:\n")
    linenum= int(input("Please Enter the Line you want the information to store:\n") )
    with open(name+".txt","r") as openfile:
        data = openfile.readlines()
    
    print(data)
    data[linenum-1]=present
    
    change=open(name+".txt","w")
    change.writelines(data)
    change.close()
    end()
    
    
    
def fileexist(n):
    l=1
    while(l==1):
        response= input("Please input what actions you want to perform with this file\nA. Read the File\nB. Delete the file and Start Over\nC. Append the File\nD. Replace a Single Line\n").lower()
        if response == "a":
            openfile= open(n+".txt","r")
            print(openfile.read())
            l=0
            openfile.close()
            end()
            
        if response == "b":
            cwd= os.getcwd()
            file_path = cwd+"\\"+n+".txt"
            os.remove(file_path)
            createfile()
            l=0
        if response == "c":
            openfile= open(n+".txt","a")
            l=0
        if response == "d":
            l=0
            update(n)
        else:
            print(" The inputted character was incorrect. Please try again.")
            
    add= input("Please Enter the information you want to put in the File\n")
    openfile.write(add+"\n")
    openfile.close()
    end()
    
def main():
    filename= input("Please Enter the Filename\n")
    check(filename)
    
def end():
    response= input("Do you want to Exit? YES or NO\n").lower()
    if response !="yes":
        main()
    else:
        return exit()
    
main()