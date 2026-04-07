from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
modified_content = content.replace('Python', 'C')
print(modified_content)