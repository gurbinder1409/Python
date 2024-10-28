
# Online Python - IDE, Editor, Compiler, Interpreter
import random
wordList=["apple","banana","pear"]
newword=random.choice(wordList)
print(newword)
dashlength=int(len(newword))
print(dashlength)
for j in range(dashlength):
    print("-",end=" ")
newString=" "
while dashlength!=0:
    guess=input("\nenter your choice")
 

    for i in newword:
        if i == guess:
            newString+=i
        
        else:
            newString+="-"
    dashlength-=1 
print(newString)
    
        
    
    
