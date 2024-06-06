import Num_Logics_Functions as nlf

def NL27():
    n=int(input("Enter a number: "))

    if nlf.Pronic(n)==1:
        print(f"Number {n} is a Pronic number")
    else:
        print(f"Number {n} is not a Pronic number")

NL27()