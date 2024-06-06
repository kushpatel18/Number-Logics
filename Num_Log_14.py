import Num_Logics_Functions as nlf

def NL14():
    n=int(input("Enter a number: "))
    # print(nlf.Armstrong(n))

    if nlf.Armstrong(n)==1:
        print(f"Number {n} is an Armstrong number")
    else:
        print(f"Number {n} is not an Armstrong number")

NL14()