#Recap on If statements

#We us if statements to run a paticular code block, based on and condition or assertion
# "I want to run this code block if ..."

#If checks a condition/assertion and if it is true will exectue a defined codeblock


#Syntax
#if (condition) :
    #indent for code block

weather = 'rainy'

assertion = (weather == 'sunny')
print(assertion)

if weather == 'sunny': #check a conditon or assertion
    print('Lets have a picnic!') #run this code if conditon is true


troch_lit = False

if troch_lit:
    print("My path is clear!")

#COMPOUND CONDITIONAL USING 'and' and 'or' logical operators

#--- and : requires that both conditons are True in order to execute our code block


#lunch window 12-13 military time
time = 12.01
hungry = True

if time == 12 and hungry:
    print('Lets grab some lunch!')

# taking it a step further by using a range

if time >= 12 and time <= 13 and hungry: #I need to be hungry AND inside my lunch hour
    print('lets go get some lunch!') # to run this code

# changing the range to be "in between"

if 13 >= time >= 12 and hungry:
    print('Lets get lunch')

#--- or: requires that at least one condition needs to be True to execute the code block

day = 'Monday'

if day == 'Saturday' or day == 'Sunday': #as long as the day is either saturday or sunday
    print('YAYYYYY its the weekend!') # run our code block

#--- Using 'and' and 'or' TOGETHER

caffinated = True
prepared_lvl = 11
confidence = 60

#how ready am I to teach
if caffinated and prepared_lvl > 6 or confidence >= 80:
    print('IM REAAADDDDYYYY to teach!')


#--- Using 'not' logical operator

#By incorporating 'not' our if statement runs off of False conditions


busy = False

if not busy:
    print('Ahhhh time to relax!')


time = 8.30

if not time < 7:
    print('I should be awake!')

#Note there are always ways to getting around using not