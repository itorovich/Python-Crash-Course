from pathlib import Path

user_name = input("Username: ")

path = Path('guest.txt')
path.write_text(user_name)