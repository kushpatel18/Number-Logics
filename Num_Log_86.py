import Num_Logics_Functions as nlf

def NL86():
    n=int(input("Enter a number: "))

    if nlf.Disarium(n)==1:
        print(f"Number {n} is a Disarium number")
    else:
        print(f"Number {n} is not a Disarium number")

NL86()