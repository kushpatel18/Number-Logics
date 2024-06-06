import Num_Logics_Functions as nlf

def NL9():
    n=int(input("Enter a number: "))

    if n>=0 :
        print(f"Factorial of number {n} is: ",nlf.factorial(n))
    else:
        print("Error! Factorial is not possible")

NL9()