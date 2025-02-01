wel="welcome to py pizza"
print(wel.center(40,'*'))
a,ex=(input('which pizza you want')),int(input("extra peporini"))
if a=='small' :
    c=15+2
    print(15+2)
elif a=='medium':
    print(20+3)
    c=20+3

else:
   c=15+3
   print(15+3)


print(f'{int(c)+ex} is your total bill ')

