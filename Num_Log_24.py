import Num_Logics_Functions as nlf

def NL24():
    n=int(input("Enter a number: "))

    if nlf.Happy(n)==1:
        print(f"Number {n} is a Happy number")
    else:
        print(f"Number {n} is not a Happy number")

NL24()