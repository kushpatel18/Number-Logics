import Num_Logics_Functions as nlf

def NL92():
    n=int(input("Enter a number: "))

    if nlf.Check_Cube(n)==1:
        print(f"Number {n} is a Perfect Cube")
    else:
        print(f"Number {n} is not a Perfect Cube")

NL92()