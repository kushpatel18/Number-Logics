import Num_Logics_Functions as nlf

def NL58():
    n=int(input("Enter a number: "))
    i=0
    temp=n
    lst=[]

    while temp>0:
        if(nlf.Neon(i)==1):
            lst.append(i)
            temp-=1
        i+=1
    # print(lst)

    print(f"The {n}th term of Neon numbers is: {lst[n-1]}")


NL58()