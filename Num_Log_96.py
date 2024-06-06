import Num_Logics_Functions as nlf

def NL96():
    n=int(input("Enter a number: "))

    if nlf.Mersenne(n)==1:
        print(f"Number {n} is a Mersenne number")
    else:
        print(f"Number {n} is not a Mersenne number")

NL96()