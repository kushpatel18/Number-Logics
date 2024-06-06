import Num_Logics_Functions as nlf

def NL28():
    n=int(input("Enter a number: "))

    if nlf.Trimorphic(n)==1:
        print(f"Number {n} is a Trimorphic number")
    else:
        print(f"Number {n} is not a Trimorphic number")

NL28()