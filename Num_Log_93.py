import Num_Logics_Functions as nlf

def NL93():
    n=int(input("Enter a number: "))

    if nlf.Cyclic(n)==1:
        print(f"Number {n} is a Cyclic number")
    else:
        print(f"Number {n} is not a Cyclic number")

NL93()