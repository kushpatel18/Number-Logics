import Num_Logics_Functions as nlf

def NL18():
    n=int(input("Enter a number: "))

    if nlf.Abundant(n)==1:
        print(f"Number {n} is an Abundant number")
    else:
        print(f"Number {n} is not an Abundant number")

NL18()