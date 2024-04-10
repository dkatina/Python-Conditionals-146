

# see what time of day it is 'night' or 'daytime'

#if it's night things get a little bit spookier
# and we start to hear some noises
#do we pick up the pace to get to our destination, or do we keep it cool and stay calm
#---maybe this becomes important later
#we see a light in the distance, do we check it out, or keep it moving
#if we made the right choices the we will succefully arrive alive

#if it's daytime
#we ask the user if they noticed how fluffy the clouds were
#do something depending on if they noticed or not
#maybe they don't arrive

#---A fun Taco adventure---

name = input('Whats your name traveler? ')
time = input("What time of day is it? 'daytime' or 'night'? ")
has_weapon = False

if time == 'night':
    #we have chosen night, things get spookier
    print('Youre walking a spooooOOoOoooky path, desprate to find some tacos.')
    choice = input("You hear some twigs break near by, do you 'pick up pace' or 'keep it cool'? ")
    if choice == 'pick up pace':
        #we chose to pick up the pace
        print('Because we chose to pick up the pace, we did not see the Magical sword just off the path.')
    elif choice == 'keep it cool':
        #we kept our cool
        print('Because you kept your cool, and your pace, you were able to notice a magical sword right off the side of the path, and you pick it up.')
        #setting our weapon variable
        has_weapon = True
    else:
        #dont be too hasty
        print('Startled you did not choose a proper action, and were eatin alive')
        print('Hesitation kills')

    choice_2 = input("As we continue down the path, we see a light in the distance, do we 'check it out' or 'keep moving'? ")
    if choice_2 == 'check it out':
        #They choose to check out the fire
        print('We arrive at a bonfire, surround by hungry goblins!')
        if has_weapon:
            #best ending beat goblins, get tacos, have cool sword
            print('Because we kept our cool and found this dope sword, we are are successfully able to fight back the goblin horde!')
            print('After your battles you continue on, and eventually make it home, where there is a taco party pack with your name on it, hot and waiting!')
            print('And you still have your cool sword')
        else:
            #traveler taco ending
            print('With nothing to defend ourselves, the goblins hastily wrap us in a tortilla and have', name, 'tacos :(')
    else:
        #mundane ending
        print('You arrive at your destination safely, and there is a taco party pack with your name on it, hot and waiting!')
        if has_weapon:
            #unless they stopped for the sword
            print('And you now have a cool sword! to go with you tacos')

    
else:
    noticed = input("With such a beautiful day, did you notice the big fluffy clouds? 'yes' or 'no' ")
    if noticed == 'yes':
        #Head in the clouds ending
        print("Preoccupied with your head in the clouds you didn't realize you were head in the wrond direction the whole time")
        print("And where never to be heard from again")
    else:
        #Pleasant but focused journey
        print("While enjoying the day, you still kept your wits about you, and safely arrived home,")
        print("with a taco party pack with your name on it, hot and waiting!")