import random

#rock wins against scissors
#paper wins against rock
#scissors wins against paper

#0 is rock
#1 is paper
#2 is scissors

rock ="🪨"
paper ="📃"
scissors="✂️"
game_images=[rock,paper,scissors]
user_input=int(input("Enter the number o to 2 to play rock,paper,scissors:"))
if user_input>=3 or user_input<0:
    print("you have entered an invalid number")
else:
    print(f"The user has chosen {game_images[user_input]}")
    comp_choice=random.randint(0,2)
    print(f"The computer chose this {game_images[comp_choice]}")
    if user_input==comp_choice:
         print("The Game is drawn")
    elif comp_choice ==0 and user_input==2:
        print("you lose")
    elif user_input==0 and comp_choice==2:
        print("you win")
    elif comp_choice > user_input:
        print("you lose")
    elif user_input > comp_choice:
        print("you win")

mylist = ['apple', 'banana', 'cherry']
create_list=[a for a in mylist if a=="banana"]
print(create_list)


a=[1,2,3,4,5,6,7,8,9,10]
b=[ azar for azar in a if azar==3]
print(b)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits[0:3])

# tuples are awesome i am gonna create and change inti the list

a=(1,2,3,4,5)
b=list(a)
print(b)
b.append(6)
b.extend([6,7,8,9,10,11,12,13,14])
a=tuple(b)
print(a)
