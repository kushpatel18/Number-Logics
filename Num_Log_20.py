import Num_Logics_Functions as nlf

def NL20():
    n=int(input("Enter a number: "))

    if nlf.Magic(n)==1:
        print(f"Number {n} is a Magic number")
    else:
        print(f"Number {n} is not a Magic number")

NL20()