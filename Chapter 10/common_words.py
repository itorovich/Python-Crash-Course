from pathlib import Path

path = Path('holy_bible.txt')
word = 'fruit '
# need to make sure to signal that the file is 
# encoded in utf-8 for outside files to avoid error
contents = path.read_text(encoding='utf-8')
count = contents.lower().count(word)

print(f'The word {word.rstrip()} appears {count} times.')