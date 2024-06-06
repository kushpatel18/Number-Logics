import Num_Logics_Functions as nlf

def NL54():
    n=int(input("Enter a number: "))
    i=1
    temp=n+1
    lst=[]

    while temp>0:
        if(nlf.Harshad(i)==1):
            lst.append(i)
            temp-=1
        i+=1
    # print(lst)

    print(f"The {n}th term of Harshad numbers is: {lst[n-1]}")


NL54()