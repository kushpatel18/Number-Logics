import Num_Logics_Functions as nlf

def NL89():
    n=int(input("Enter a number: "))

    if nlf.Duck(n)==1:
        print(f"Number {n} is a Duck number")
    else:
        print(f"Number {n} is not a Duck number")

NL89()