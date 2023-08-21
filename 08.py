#The only form of nesting we've encountered so far was an if statement within a loop.
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C#":
        print(language + " found")
        break

#proper nesting is vital inside of python. Unlike many other languages,
#python is indentation sensitive. The position of the code is important

for language in languages:
    if language == "C#":
        print(language + " found")
    break

#^^ This loop does something completely different.
#Syntactically, the only difference is the position of the break keyword. 
#It will break at the end of the first iteration no matter what

########## NESTED IF ##########

logging = True
logging_in = True
name = "Caleb"

if logging_in:
    if logging:
        print(name + " is logging in.") #log console, file, or db.
    print("Welcome, " + name)

########## CONVERTING COMPLEX CONDITIONAL TO NESTED IF ###########

#It is common in more complex code to see nested if statements
#This can often replace complex expressions that use numerous logical operators
#Either way is not better, just whatever is clearer to you 

age = 20
fun = False
likes_to_dance = True

if (age < 30 or fun) and likes_to_dance:
    print("You're invited to the party!")
else:
    print("get lost freakbag") #most general

#This could alternatively be represented with nested if statements 
#and can allow more specific responses

if age < 30 or fun:
    if likes_to_dance:
        print("You're invited to the party!")
    else:
        print("How could you not like to dance?") #Specific to dancing
else:
    print("You're either too old or not fun enough to be in my party")
    #Note how we can't easily say which. We say OR.


########## INTRO TO NESTED FOR ##########

#If you are fairly new, nested loops can be confusing. Pay attention!
#Stop texting and looking at memes...CODE!
#We can loop a loop using a nested loop.
#The inner loop will run each iteration of the outer loop.

for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print() #go to next line

#The result? The inner loop prints 0 - 4. We then do this 4 times
#After each complete 0-4 print, we go to the next line with print()
#This puts the next loop on the next line of output

########## NESTED FOR LOOP PT2 ###########


#The previous section had this loop. 
#The only thing we did was print j and a new line.
for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print() #go to next line

#Review this and make sure you understand what is going on.

#We could also say what iteration of the outer loop we are on
for i in range(4):
    print("iteration " + str(i), end=": ")
    for j in range(5):
        print(j, end=" ")
    print() #go to next line

#We could also do a more complicated loop to work with the numbers.
for i in range(4):
    print("Count by " + str(i), end=": ")
    for j in range(5):
        print(j*i, end=" ")
    print("...") #go to next line

#What's going on here? 
#We are taking the outer iteration variable and multiplying to by the inner
#in other words, we are counting to 5 each time
#but we are multiplying the result by 0, 1, 2, 3

########## OUTER LOOP VARIABLES IN INNER range() - TRIANGLES #########

#I had no idea what to call this section. Whatever.

#We can always use the outer loop iteration variable within the inner loop.
#What if we wanted to count to 9 for each iteration,
#but start with a higher number each time?

for i in range(10):
    for j in range(i, 10):
        print(j, end=" ")
    print()

#The first iteration i will be 0, so we get: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#The second iteration i will be 1, so we get 1, 2, 3, 4, 5, 6, 7, 8, 9
#etc. 


########## NESTED WHILE ##########


#We now have to worry bout the initialization and increment.

#print 0-4, 4 times:
i = 0
while i < 4:
    j = 0
    while j < 5:
        print(j, end=" ")
        j += 1
    print()
    i += 1

#not as clean...initialization and inrement has to be correct
#pay close attention

#This won't work as expected:

print("Let's try this again:")
i = 0
j = 0
while i < 4:
    while j < 5:
        print(j, end=" ")
        j += 1
    print()
    i += 1

print("What happened?") #j is never reset back to zero


########## LOOP TO SUM ALL NUMBERS ##########


#I want to calculate the sum of numbers 0-10: 10+9+8+7+6+5+4+3+2+1

sum = 0
j = 10
while j > 0:
    sum += j
    j -= 1
print(sum) #55 

#But now I want to get the sum of 9-0, 8-0, 7-0, 6-0, etc...
#Here will be the structure:

i = 10
while (i > -1): #include zero. Could also do >= 0
    #print sum from i to zero. 
    i -= 1


#We just coded how to sum to zero...so copy/paste that there....
#change to j = i (dynamic from 10 to 0)
print("All the sums:")
i = 10
while (i > -1): 
    sum = 0
    j = i
    while j > 0:
        sum += j
        j -= 1
    print(sum) 
    i -= 1

#We can now customize the output to be more readable:
print("All the sums with output:")
i = 10
print("Getting sums up to", i)
while (i > -1): 
    sum = 0
    j = i
    while j > 0:
        if j > 1:
            print(j, "+", end=" ")
        else:
            print(j, "=", end=" ")
        sum += j
        j -= 1
    print(sum) 
    i -= 1