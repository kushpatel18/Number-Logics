import Num_Logics_Functions as nlf

def NL11():
    n=int(input("Enter a number: "))
    rev=nlf.Reverse_Num(n)
    # print(rev)
    if n==rev:
        print(f"Number {n} is palindrome: ")
    else:
        print(f"Number {n} is not palindrome")

NL11()