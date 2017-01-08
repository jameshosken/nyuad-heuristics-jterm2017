#Prints numbers 1 to 100

#Replaces numbers divible by 3 with 'fizz'
#Replaces numbers divible by 5 with 'buzz'
#Replaces numbers divible by 3 and 5 with 'fizzbuzz'

#First trick is to count to 101; that will include number 100
for i in range(1,101):
    #First check for the "both" condition:
    if(i%3==0 and i%5== 0):
        print("fizzbuzz")
    #If not both, then check for the at 'either' conditions:
    elif(i%3==0):
        print("fizz")
    elif(i%5== 0):
        print("buzz")
    #If neither, just print the number:
    else:
        print(i)
    