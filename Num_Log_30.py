import Num_Logics_Functions as nlf

def NL30():
    m=int(input("Enter lower range: "))
    n=int(input("Enter upper range: "))
    lst=[]

    for i in range(m,n+1):
        if(i==nlf.Reverse_Num(i)):
            lst.append(i)

    print(f"Palindrome Numbers within the range of {m} to {n} are: {lst}")

NL30()
