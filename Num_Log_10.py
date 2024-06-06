import Num_Logics_Functions as nlf

def NL10():
    n=int(input("Enter a number: "))

    if n>0 :
        print(f"Prime Factors of number {n} are: ",nlf.Prime_Factors(n))
    else:
        print("Prime Factorization is not possible")

NL10()