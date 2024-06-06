import Num_Logics_Functions as nlf

def Compute1():
    n=int(input("Enter a number: "))
    if n>=0:
        print(f"Value of 1/n! is: ",1/nlf.factorial(    n))
    else:
        print("Error! Enter a valid positive number")

Compute1()