import random

path = 'session16/part02/data.txt'
wincard = {'p': 's', 'r': 'p', 's': 'r'}
counter = 0
pcwin = 0
hwin = 0

# x = [item for item in wincard.keys()]
# print(x)

with open(path, 'w') as f:
    while True:
        pc_choice = random.choice([item for item in wincard.keys()])
        # print(pc_choice)
        human_choice = input('select from r/p/s: ')

        if human_choice == 'end':
            break
        elif human_choice == pc_choice:
            print('same choice, please try again')
            continue
        elif human_choice not in [item for item in wincard.keys()]:
            print('is not valid, try again')
            continue
        elif human_choice == wincard.get(pc_choice):
            print('you won!')
            hwin += 1
        else:
            print('you lost!')
            pcwin += 1


        counter += 1
        f.write(f'{counter}: p: {pc_choice}, h: {human_choice}\n')
    f.write(f'\npc: {pcwin}\nhuman: {hwin}')



