import Num_Logics_Functions as nlf

def NL53():
    n=int(input("Enter a number: "))
    i=0
    temp=n+1
    lst=[]

    while temp>0:
        if(nlf.Perfect(i)==1):
            lst.append(i)
            temp-=1
        i+=1
    # print(lst)

    print(f"The {n}th term of Perfect numbers is: {lst[n-1]}")


NL53()