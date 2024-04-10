#Inline if statements aka Ternary Operators are simply a way to write if statements
#in a single line

#Syntax
#if_output if (condition) else else_output

#Why? allows to have concise conditionals within a single line

candy_jar = 'empty'

print('Its Candy Time!' if candy_jar == 'full' else 'Time to hit up Mr. Wonka!')

#ternary operator with 'and'

candy_jar = 'empty'
sweet_tooth = True

print('Its Candy Time!' if candy_jar == 'full' and sweet_tooth else 'Who needs candy anyway')

#ternary operator with 'or'

day = 'Tuesday'
print('Its the weekend') if day == 'Saturday' or day == 'Sunday' else print('BOOOOOOOOO its the work week')