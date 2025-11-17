import re

file_path = r"C:\Users\ASUS\Desktop\all in\IUCA\python\лаба 10\mockdata.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Имена — первое слово в каждой строке
names = re.findall(r'^(\w+)', text, flags=re.MULTILINE)

# Фамилии — второе слово в строке
surnames = re.findall(r'^\w+\s+(\w+)', text, flags=re.MULTILINE)

# Типы файлов — всё, что идёт после точки
types = re.findall(r'\.(\w+)\b', text)

print("Имена:")
print(*names, sep="\n")

print("\nФамилии:")
print(*surnames, sep="\n")

print("\nТипы файлов:")
print(*types, sep="\n")
