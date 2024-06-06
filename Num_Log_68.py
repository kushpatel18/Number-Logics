import Num_Logics_Functions as nlf

def NL68():
    n=int(input("Enter a number: "))
    count_1=0
    count_0=0

    count=nlf.Count_1_0(n,count_1,count_0)

    for i in range(0,len(count)):
        if i==0:
            print(f"Number of 1s in {n} are: {count[i]}")
        if i==1:
            print(f"Number of 0s in {n} are: {count[i]}")

NL68()