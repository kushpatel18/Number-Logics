import Num_Logics_Functions as nlf

def NL70():
    n=int(input("Enter a number:"))
    max_digit=0

    max_digit=nlf.Max_Digit(n,max_digit)
    print(f"Max digit of number {n} is: {max_digit}")

NL70()