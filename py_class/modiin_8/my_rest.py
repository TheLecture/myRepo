from random import randint
restaurant = {'chef': 1, 'waiters': 2, 'Tables': 20}
price = {
    'salad': 25,
    'bread': 20,
    'soup': 30,
    'beef steak': 120,
    'wings': 100,
    'pasta': 90,
    'chocolate cake': 80,
    'Ice cream': 50,
    'lemon pie': 70,
    'cola': 15,
    'water': 10,
    'fuzeTea': 20,
    'Beer': 30
}

def chef(request):
    ran = ['send', 'The batch is burnt send again please 🔥']
    starters = ['salad', 'bread', 'soup']
    main_courses = ['beef steak', 'wings', 'pasta']
    desserts = ['chocolate cake', 'Ice cream', 'lemon pie']
    drinks = ['cola', 'water', 'fuzeTea', 'Beer']
    
    if request == 'food menu':
        return {'starters': starters, 'main courses': main_courses, 'desserts': desserts}
    elif request == 'drink menu':
        return drinks
    
    for items in [starters, main_courses, desserts]:
        for item in items:
            if request == item:
                x = randint(0, 100)
                if x > 85:
                    x = 1
                else:
                    x = 0
                return ran[x]

def host():
    if restaurant['Tables'] > 0:
        restaurant['Tables'] -= 1
        return chef('food menu'), chef('drink menu')
    else:
        print('The restaurant is full!! Please wait...')

def waiters():
    req = input('Please enter your choice : ')
    if req == 'account please':
        total_price = 0
        while True:
            item = input('Enter the item (type "done" when finished): ')
            if item == 'done':
                break
            if item in price:
                total_price += price[item]
            else:
                print("Item not found in the menu!")
        print(f'Total bill: ${total_price}')
    else:
        print(chef(req))

if __name__ == "__main__":
    print(chef('soup'))  # Test chef function
