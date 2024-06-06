import Num_Logics_Functions as nlf

def NL7():
    n=int(input("Enter first number: "))
    m=int(input("Enter second number: "))

    if n>0 and m>0:
        print(f"HCF/GCD of number {n} and {m} is: ",nlf.HCF(n,m))
    else:
        print("HCF/GCD is not possible")

NL7()