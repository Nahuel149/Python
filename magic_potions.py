# Assignment 6: The Magic Potion Shop

potions = { 
    "HP": ["Moonstone", "Dragon scale", "Fairy dust"], 
    "MP": ["Phoenix feather", "Troll tooth", "Mermaid scale"], 
    "SP": ["Unicorn horn", "Elf hair", "Golden apple"] 
    }

print(" ")
print('Welcome to the Magic Potion Shop!')
print('Here are the potions we offer: ')
for potion in potions.keys():
    print(potion)

print(" ")
choose_potion = input(f'Which potion would you like to buy ingredients for? ').upper().replace(" ", "")
if choose_potion in potions:
    print(f'The ingredients for {choose_potion} are: ')
    for ingredients in potions[choose_potion]:
        print(ingredients)
else: 
    print(f'Sorry, we do not have ingredients for {choose_potion}.')
print(" ")

if choose_potion in potions:
    print('Let\'s start buying the ingredients!')

bought_count = 0
while bought_count < 3:
    ingredients = potions[choose_potion][bought_count]
    shop = input(f'Do you want to buy {ingredients} (yes/no): ').lower().replace(" ", "")
    if shop == 'no':
        print('You choose to stop shopping!')
        break
    elif bought_count == 2:
        print(f'You Bought {ingredients}!')
        print(" ")
        print(f'Congratulations! You bought all the ingredients for {choose_potion}!')
        break
    else:
        print(f'You Bought {ingredients}!')
        bought_count += 1