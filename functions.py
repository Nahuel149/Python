# def dollarizer():    
#     print(input('This will replace any word that contains S for $; ').replace('s', '$'))

# def eurizer():
#     print(input(f'This will replace any word that contains e for €; ').replace('e', '€'))

# char1 = input('Choose the character you want to replace, for example (e): ')
# char2 = input('Choose the new character that will replace the previous one, for example (€): ')

# def replacer():
#     print(input(f'Choose your words now: ').replace(char1, char2))

# replacer()

# def wonky_text():
#     print(input(f'This will replace any word that contains l for £; ').replace('l', '£'))
#     return dollarizer(), eurizer()

# wonky_text()

# def celsius_to_fahrenheit():
#     C = int(input('Choose temperature in celsius: '))
#     F = C * 9//5 + 32
#     print(f'Your temperature in farenheit is: {F}')
    
# celsius_to_fahrenheit()

# def age_in_days():
#     Year = int(input(f'How many years old are you? '))
#     Day = Year * 365
#     print(f'You are {Day} days old')

# age_in_days()

def simple_interest():
    P = int(input('Write how much is the debt: '))
    R = 0.1
    T = int(input('The plan to pay is in how many years? '))
    SI = P * R * T
    print((f'The total interest with debt is: ${SI:,.2f}'))
    return SI

simple_interest()

def plan_finances():
    SI = simple_interest ()
    desired = SI * 0.91
    print(f'The new desired ammount is: ${desired:,.2f}')
    return desired

plan_finances()