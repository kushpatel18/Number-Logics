import Num_Logics_Functions as nlf

def NL75():
    n=int(input("Enter a number: "))

    count=nlf.Odd_Even_Count(n)

    for i in range(0,len(count)):
        if i==0:
            print(f"Number of odd digits in {n} are: {count[i]}")
        if i==1:
            print(f"Number of even digits in {n} are: {count[i]}")

NL75()