#If statements are our original condition
# Elif allows us to chain on additonal conditions/assertions, with corresponfing
#code blocks to 

#the flow of the if elif chain is top down, and as soon as a conditon evaluates
# to true that coee block is ran and the rest of the condtions are skipped

money = 15


if money >= 50:
    print('Lets have a nice steak dinner')
elif money >= 20:
    print('Italian sounds like a good choice!')
elif money >= 10:
    print('Lets grab chipotle!')

#Else statements, essentially a default condtion. They dont have a specific condition of their own
#but if none of the other conditions evaluate to True, than the else code block runs

#you'll only have one else per if chain
# it will always be at the very end

money = 8
1
if money >= 50:
    print('Lets have a nice steak dinner')
elif money >= 20:
    print('Italian sounds like a good choice!')
elif money >= 10:
    print('Lets grab chipotle!')
else:
    print("I probably should just cook at home :(")