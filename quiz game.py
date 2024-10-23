print("Welcome to my computer quiz!")

playing = input("Do you want to play yes or no:?")

if playing.lower() !="yes":
    print("Okay see you someother time! have a great day ahead !")
    quit()
else:
    print("Okay! Lets play :)")
score = 0



answer=input("what does cpu stand for? ")

if answer.lower()=="central processing unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")

answer=input("what does ram stand for? ")

if answer.lower()=="random access memory":
    print("correct!")
    score +=1
else:
    print("Incorrect!")
answer=input("what does gpu stand for? ")

if answer.lower()=="graphic processing unit":
    print("correct!")
    score +=1
else:
    print("Incorrect!")

answer=input("what does love stand for? ")
if answer.lower() =="caring":
    print("correct!")
    score +=1
else:
    print("Incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)*100) + "%.")

