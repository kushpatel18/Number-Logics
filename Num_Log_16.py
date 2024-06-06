import Num_Logics_Functions as nlf

def NL16():
    n=int(input("Enter a number: "))

    if nlf.Perfect(n)==1:
        print(f"Number {n} is a Perfect number")
    else:
        print(f"Number {n} is not a Perfect number")

NL16()