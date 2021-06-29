import random
import math

wordlist=['bat','sit','key','lip'];

#This is a demo wordlist. A bigger wordlist can be put in the code according to requirement

string_index = random.randint(0,len(wordlist)-1)

string = wordlist[string_index]
print("Guess a",len(string),"letter word.")

tries = round(math.log(len(wordlist[string_index])))

if(tries<3):
    tries=3

correctcounter = 0
incorrectcounter = 0

while tries!=0:
    print("You have",tries,"tries left")
    c=input("Guess a letter: ")
    for j in string:
        if c==j:
            print(c,end=" ")
            correctcounter+=1
        else:
            print("_",end=" ")
            incorrectcounter+=1
    if int(incorrectcounter)==3:
        tries-=1
    if int(correctcounter)==len(string):
        print("\nYou have guessed correctly!")
        break
