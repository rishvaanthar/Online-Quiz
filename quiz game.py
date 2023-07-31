print("Welcome to my computer quiz")

playing=input("Do you want to play: ").lower()

if playing!="yes":
    quit()

print("Okay! Let's play :) ")
score=0
answer=input("What does CPU stands for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does PSU stands for ").lower()
if answer=="power supply":
    print("Correct!") 
    score+=1
else:
    print("Incorrect!") 

answer=input("What does GPU stands for: ").lower()
if answer=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input ("Which is the most powerful processor in a laptop?: ").lower()
if answer=="AMD ryzen 9":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")   
print("You got " + str((score/4)*100) + "%.")   

