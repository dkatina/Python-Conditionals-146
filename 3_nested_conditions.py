#In python we can have nested if's, or if statements inside if statements

#Activity of the day

#nested ifs allow us to check conditions based on another condition being true
#inner ifs are dependent on outer condition being true

weather = 'cloudy'
friends_and_i = 2

if weather == 'sunny': # outter condition
    #inner ifs 
    if friends_and_i >= 6:
        print('Lets play vollyball')
    elif friends_and_i == 5:
        print('Lets play frisbee')
    else:
        if friends_and_i == 1:
            print('I think Ill play some golf...all by my lonesome :(')
        else:
            print('The', friends_and_i, 'of us, should play golf!')
else:
    print('Lets go to the movies')