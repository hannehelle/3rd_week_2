with open('referat.txt', 'r') as file:
    content = file.readlines()
    fullStr = ' '.join(content)

print(f'Длина строки: {len(fullStr)} символов')
print(f'В тексте {len(fullStr.split(" "))} слов')

with open('2referat.txt', 'w', encoding='utf-8') as f:
    new_fullstr = fullStr.replace(".", "!")
    f.write(new_fullstr)