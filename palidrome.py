def reverse(n):
    rev=n%10    
    n=n//10

    while (n>0):
        r=n%10
        n=n//10
        rev=rev*10+r
    return(rev)   #return shoud be use not print

num=abs(int(input("entr num :")))
if reverse(num)==num:
    print("palidrome")
else:
    print("not palidrome")