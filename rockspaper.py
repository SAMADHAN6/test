import random
rock ='''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
r=random.randrange(0,3)
j=random.randrange(0,3)
p1=(game[r])#here i take two players
p2=game[j]

if p1=='rock' and p2=='scissors':
    print("p1 win \n p1 loss")

elif p1=='scissors' and p2=='paper':
    print("p1 win \n p1 loss")

elif p1=='paper' and p2=='rock':
    print("p1 win \n p1 loss")
elif p1==p2:
    print('play agian')
else:
    print("p2 win \n p1 loss")