import pyinputplus as pyip, re

menu = [{'wheat': '1.1 £', 'white': '2.4 £', 'sourdough': '3.2 £'},
        {'beef': '1.5 £', 'turkey': '2.23 £', 'ham': '3.34 £', 'tofu': '4.34 £'},
        {'cheddar': '1.56 £', 'stilton': '2.39 £', 'mozzarella': '3.67 £'},
        {'brown sauce': '0.23 £', 'salad dressing': '0.45 £', 'tomato sauce': '0.59 £'},
        {'lettuce': '0.12 £', 'tomato': '0.16 £', 'onion': '0.23 £'}]

menuText = ['Enter a bread type:',
            'Enter a main topping:',
            'Do you want cheese?(y/n)',
            'Do you want any sauce?(y/n)',
            'Do you want vegetables?(y/n)',
            'How many sandwiches do you want?:']
                 
order = []
totalCost = 0
def pyIP(text, choice, yn):
    if text:
        print(text)
    if yn == True:
        return pyip.inputYesNo(prompt='')
    elif yn == False:    
        return pyip.inputMenu(
            [k + ' ' + v for k, v in menu[choice].items()], 
            numbered=True, prompt='')
    elif yn == 'end':
        return pyip.inputInt(min=1, prompt='')
        
for i in range(len(menuText)):
    if i <= 1:
        order.append(pyIP(menuText[i], i, False))
    elif i in range(2,5):
        if pyIP(menuText[i], i, True) == 'yes':
            order.append(pyIP('', i, False))
    elif i == 5:
        totalSandwiches = pyIP(menuText[i], i, 'end')
        
for i in [re.sub(r'[^0-9.]', '', i) for i in order]:
    totalCost += float(i) * totalSandwiches

print(f'Total price: {round(totalCost, 2)} £')

if totalCost > 50:
    print('Those are some expensive sandwiches!')