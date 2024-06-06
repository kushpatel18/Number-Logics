import Num_Logics_Functions as nlf

def Num_Logics_3():
    x=int(input("Enter a number: "))
    num=int(input("Enter a number: "))

    if(num>=0):
        print(f"Value of x^n/n! is: ",x**num/nlf.factorial(num))
    else:
        print("Error! Enter a valid positive integer")

Num_Logics_3()