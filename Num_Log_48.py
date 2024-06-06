import Num_Logics_Functions as nlf

def NL48():
    n=int(input("Enter a number: "))
    i=0
    temp=n+1
    lst=[]

    while temp>0:
        if(nlf.Reverse_Num(i)==i):
            lst.append(i)
            temp-=1
        i+=1
    # print(lst)

    print(f"The {n}th term of Palindrome numbers is: {lst[n-1]}")


NL48()