import Num_Logics_Functions as nlf

def NL76():
    n=int(input("Enter a number: "))

    if(nlf.Ugly(n)==1):
        print(f"Number {n} is an ugly number")
    else:
        print(f"Number {n} is not an Ugly number")

NL76()