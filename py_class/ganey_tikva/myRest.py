from random import randint

restaurant = {'chef': 1, 'waiters': 2, 'Tables': 20}
price = {}


def chef(request):
    ran = ['send', 'The batch is burnt send again please 🔥']
    foodMenu = {'First': ['salad', 'bread', 'soup'], 'Main': ['beef steak', 'wings', 'pasta'],
                'dessert': ['chocolate cake', 'Ice cream', 'lemon pie']}
    drinkMenu = ['cola', 'water', 'fuzeTea', 'Beer']
    if request == 'food menu':
        return foodMenu
    elif request == 'drinks  menu':
        return drinkMenu
    for i in foodMenu.values():
        for j in range(3):
            if request == i[j]:
                x = randint(0, 100)
                if x > 85:
                    x = 1
                else:
                    x = 0
                return ran[x]

def host():
    if restaurant['Tables'] > 0:
        restaurant['Tables'] -=1
        return chef('food menu'),chef('drink menu')
    else:
        print('The restaurant is full!! wait please ...')

def waiters(nt):
    req = input('Please enter your choice : ')
    print(chef(req))
    if req == 'account please':
        return None
        
        

print(chef('soup'))