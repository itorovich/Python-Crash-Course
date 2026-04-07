from pathlib import Path

path = Path('guest_book.txt')

session = True
contents = ''

while session:
    guest_name = input('What is your name? To end session write End: ')

    if guest_name == 'End':
        session = False

    else:
        # contents = '' 
        # had that line above in originally and it was causing my variable
        # to reset back to an empty string whenever it would go through the loop again
        contents += f'{guest_name}\n'

path.write_text(contents)

        

    
