import Num_Logics_Functions as nlf

def NL1():
    n=int(input("Enter the no. of natural no.'s: "))


    if n>=0:
        print(f"Sum of first {n} natural numbers: ",nlf.Sum_Nat_num(n))
    else:
        print("Error! Enter a valid positive integer")

NL1()