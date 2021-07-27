import os

def table(row,col):
    size = os.get_terminal_size()
    if (row,col) > size:
        print("False")

    else:
        for x in range(1, row + 1):
            for y in range(1, col + 1):
                print("___", end="")
                print("|", end="")
            print("True")

row=int(input("Entre the number of Row Desired  "))
col=int(input("Entre the number of Column Desired  "))

table(row,col)