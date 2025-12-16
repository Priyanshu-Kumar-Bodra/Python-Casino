import random as rd

rules1 = '''This is a simple slot machine.
You can see 3 rows in front of you. Only the middle row is important.'''

rules2 = '''You will be awarded prize money based on what combination of the following symbols
you get on the middle row.
Denomination: 1 credit per dollar($).
First you enter a certain amount of money.
Then for each round, you choose how many credits are you betting.
For 1 credit round:
    2x 2x 2x : 1600
    7  7  7  : 100
    $  $  $  : 30
    =  =  =  : 20
    1  1  1 / O  O  O : 10
    1  =  $ (any 3 mixed) / O (any two) : 5
    O (any one) : 2
2 credit round unlocks 5x:
    5x 5x 5x : 2500
    2x 5x (any 3 mixed) : 1000
3 credit round unlocks 10x:
    10x 10x 10x : 10000
    2x 5x 10x (any 3 mixed) : 1000
Bonus: 2x, 5x and 10x multipliers anywhere multiply your winnings by that number
2 5x multipliers would multiply the winnings by 25
You can quit anytime and walk away with the remaining money'''


def print_slot_machine (A: list, B: list, C: list):
    print(f'| {A[0]:^3} | {A[1]:^3} | {A[2]:^3} |')
    print(f'| {B[0]:^3} - {B[1]:^3} - {B[2]:^3} |')
    print(f'| {C[0]:^3} | {C[1]:^3} | {C[2]:^3} |')


symbol_list = [' ', 'O', '1', '=', '$', '7', '2x', '5x', '10x']

def random_generator(c: int):
    ABC = []
    prob_dict = {' ': 600, 'O': 750, '1': 900, '=': 950, '$': 975, '7': 990, '2x': 1000}
    if c == 2:
        prob_dict['2x'] = 996
        prob_dict['5x'] = 1000
    elif c == 3:
        prob_dict['2x'] = 995
        prob_dict['5x'] = 998
        prob_dict['10x'] = 1000

    #prob_dict = {' ': 200, 'O': 300, '1': 400, '=': 500, '$': 600, '7': 700, '2x': 800, '5x': 900, '10x': 1000}

    for i in range(9):
        slot_val = rd.randint(1,1000)
        for sym in symbol_list:
            if (slot_val <= prob_dict[sym]):
                ABC.append(sym)
                break
    return (ABC)


reward_dict = {' ': 0, 'O': 10, '1': 10, '=': 20, '$': 30, '7': 100, '2x': 1600, '5x': 2500, '10x': 10000}
mix1 = {'1', '=', '$'}
mix2 = {'2x', '5x'}
mix3 = {'2x', '5x', '10x'}

def reward_calc(grd: list):
    a, b, c = grd[3], grd[4], grd[5]
    mset = {a, b, c}
    if (len(mset) == 1):
        reward = reward_dict[a]
    elif (mset <= mix1):
        reward = 5
    elif (mset <= mix2):
        reward = 1000
    elif (mset <= mix3):
        reward = 1000
    elif (len(mset) == 3):
        if ('O' in mset):
            reward = 2
        else:
            reward = 0
    elif ((a == b and a == 'O') or (b == c and b == 'O') or (a == c and a == 'O')):
        reward = 5
    else:
        reward = 0
    
    multiplier = 1
    count2, count5, count10 = 0, 0, 0
    mult_check = grd[:3] + grd[6:]
    if reward <= 100:
        mult_check = grd
    for symbl in mult_check:
        if symbl == '2x':
            count2 += 1
        elif symbl == '5x':
            count5 += 1
        elif symbl == '10x':
            count10 += 1
    multiplier *= (2**count2)*(5**count5)*(10**count10)
    return (reward*multiplier)
    


opt = input('Would you like to know the rules? (enter yes or no): ')
if opt.lower() == 'yes':
    print(rules1)
    print_slot_machine(['=',' ','O'], [' ', '$', '1'], ['2x', '=', '='])
    print(rules2)

total = int(input('Enter the betting amount: $'))
print('Credits remaining:', total)

while True:
    print('Press q if you would like to quit')
    cred = input('How many credits (1, 2 or 3): ')

    if (cred == 'q' or cred == 'Q'):
        print(f'You walk away with ${total}')
        break 

    valid = 'qQ123'
    if cred not in valid:
        print('Please enter a valid number or q')
        continue

    cred = int(cred)
    if (cred > total):
        print('Not enough credits')
        continue
    total -= cred

    grid = random_generator(cred)
    print_slot_machine(grid[:3], grid[3:6], grid[6:])
    reward = reward_calc(grid)

    print('You spent', cred, 'and earned', reward)
    total += reward
    print('Credits remaining:', total)

    if (total <= 0):
        print('You ran out of credits')
        break

print('Thank you for playing the slot machine')

