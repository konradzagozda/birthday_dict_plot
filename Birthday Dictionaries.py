import json

try:
    with open("info.json", 'r') as fh:
        birthdays = json.load(fh)
except FileNotFoundError:
    birthdays = {
        'Ania Kwidzinska': '18/03/2000',
        'Konrad Zagozda': '22/02/1995',
    }
    with open("info.json", "w") as fh:
        json.dump(birthdays, fh)

while True:
    add = input('Do you want to add another person to our dictionary?(y/n)').lower()
    if add == 'y':
        name = input('Tell me name of the person: ')
        date = input('Tell me date of birth (DD/MM/YYYY)')
        birthdays[name] = date
        with open("info.json", 'w') as fh:
            json.dump(birthdays, fh)
    elif add == 'n':
        break


print('Welcome to the birthday dictionary. We know the birthdays of:')
print('\n'.join(birthdays.keys()))
while True:
    name = input('Who\'s birthday do you want to look up?(say quit to quit)')
    if name == 'quit':
        break
    if name in birthdays:
        print(f'{name}\'s birthday is {birthdays[name]}')
    else:
        print('You have to be exact with the name')

