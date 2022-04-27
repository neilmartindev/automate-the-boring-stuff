while True:
    print('Who are you?')
    name = input()
    print('What is your age?')
    age = int(input())
    if name == 'Alice' and age == 24:
        print('Hi, Alice.')
    elif age <= 12:
        print('You are not Alice, kiddo.')
    elif age > 100 and age < 1999:
        print('You are not Alice, grannie.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')

    break