import os
os.system('clear')
h = input('\033[1;36m File Name Plz: \033[0m')
if h == 'm.txt':
    print('\033[1;34m ')
    t = open('m.txt', 'r')
    print(t.read())
    print(os.path.getsize('m.txt'))
else:
    print('Try Again')

