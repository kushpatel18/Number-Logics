import Num_Logics_Functions as nlf

def NL15():
    n=int(input("Enter a number: "))

    if nlf.Strong(n)==1:
        print(f"Number {n} is a Strong number")
    else:
        print(f"Number {n} is not a Strong number")

NL15()