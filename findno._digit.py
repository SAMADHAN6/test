def finddigit(num):
    d=1
    i=0
    while (num>9):
        num=num//10
        d+=1
    print(d)
def reverse(n):
    rev=n%10    
    n=n//10

    while (n>0):
        r=n%10
        n=n//10
        rev=rev*10+r
    print(rev)



num=abs(int(input("enter the no__")))
finddigit(num)
reverse(num)

