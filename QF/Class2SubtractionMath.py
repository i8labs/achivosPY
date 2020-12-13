
import random

f = open("Class2Subtraction.txt", "w")

NumofSubQuestions = 10
print("Subject: 10012", file=f)
print("Class: 2", file=f)
print("Chapter: 10077", file=f)
print("Type: FIB", file=f)
print("Complexity: 1", file=f)
print("Marks: 1", file=f)
print("", file=f)


NumofSubQuestions = 15 

for i in range(NumofSubQuestions):
    num1 = random.randint(851,950)
    num2 = random.randint(101,850)
    print("Q:) Subtract the following  %3d  -  %3d  "%(num1,num2), file=f)
    print("answer: %d"%(num1-num2), file=f)
    print("", file=f)

num1 = random.randint(851,950)
num2 = random.randint(101,850)
subWP="Q:) A factory produced "+str(num2)+" gas stoves in a year and  " + str(num1) + " gas stoves in the following year. Find the increase in production of gas stoves? " 
print(subWP, file=f)
print("answer: %d"%(num1-num2), file=f)
print("", file=f)

num1 = random.randint(851,950)
num2 = random.randint(101,850)
subWP="Q:) Tejas read "+str(num2)+" pages of his book before lunch. After lunch he read some more. If Tejas read  " + str(num1) + " pages in all than how many pages did he read after lunch?" 
print(subWP, file=f)
print("answer: %d"%(num1-num2), file=f)
print("", file=f)

num1 = random.randint(851,950)
num2 = random.randint(101,850)
subWP="Q:) There are "+str(num1)+" people watching the soccer game." + str(num2) + " of them are adults. How many kids are watching the game?" 
print(subWP, file=f)
print("answer: %d"%(num1-num2), file=f)
print("", file=f)

num1 = random.randint(851,950)
num2 = random.randint(101,850)
subWP="Q:) There are "+str(num1)+" people watching the soccer game." + str(num2) + " of them are adults. How many kids are watching the game?" 
print(subWP, file=f)
print("answer: %d"%(num1-num2), file=f)
print("", file=f)

num1 = random.randint(851,950)
num2 = random.randint(101,850)
subWP="Q:) A string of light has "+str(num1)+" light bulbs out of which " + str(num2) + " are broken. How many light bulbs are in working condition?" 
print(subWP, file=f)
print("answer: %d"%(num1-num2), file=f)
print("", file=f)

num1 = random.randint(851,950)
num2 = random.randint(101,850)
subWP="Q:) Rajan invited "+str(num1)+" guests to his marriage. Only " + str(num2) + " guests came to the marriage. How many guets did not come?" 
print(subWP, file=f)
print("answer: %d"%(num1-num2), file=f)
print("", file=f)

num1 = random.randint(851,950)
num2 = random.randint(101,850)
subWP="Q:) A book had  "+str(num1)+" pages. Arayn read " + str(num2) + " form the book. How many pages are reamining for Aryan to read ?" 
print(subWP, file=f)
print("answer: %d"%(num1-num2), file=f)
print("", file=f)



f.close()