while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    elif password !='swordfish':
        print('Access Denied, you are not Joe')
        quit()
print('Access granted.')

