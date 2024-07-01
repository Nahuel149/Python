fruit_dict = {}

while True:
    fruit_input = input(f'Enter an item (or "done" to finish): ')
    if fruit_input.lower() == 'done':
        break
    else:
        if fruit_input in fruit_dict:
            fruit_dict[fruit_input] += 1
        else:
            fruit_dict[fruit_input] = 1
    
print('Item counts:')
print(fruit_dict)