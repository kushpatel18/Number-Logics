import Num_Logics_Functions as nlf

def NL23():
    n=int(input("Enter a number: "))

    if nlf.Spy(n)==1:
        print(f"Number {n} is a Spy number")
    else:
        print(f"Number {n} is not a Spy number")

NL23()