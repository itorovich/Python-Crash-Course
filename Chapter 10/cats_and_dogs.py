from pathlib import Path

list = ['cats.txt', 'dogs.txt', 'birds.txt']

for file in list:
    path = Path(file)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        # print(f'Sorry {file} does not exist')
        pass
    else:
        print(contents)
