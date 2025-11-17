import re

file_path = r"C:\Users\ASUS\Desktop\all in\IUCA\python\лаба 10\mockdata.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

def extract_names(text):
    return re.findall(r'^(\w+)', text, flags=re.MULTILINE)

def extract_surnames(text):
    return re.findall(r'^\w+\s+(\w+)', text, flags=re.MULTILINE)

def extract_file_types(text):
    return sorted(set(re.findall(r'\.(\w+)\b', text)))

names = extract_names(text)
surnames = extract_surnames(text)
file_types = extract_file_types(text)

print("Имена:")
for n in names:
    print(f"- {n}")

print("\nФамилии:")
for s in surnames:
    print(f"- {s}")

print("\nТипы файлов:")
for t in file_types:
    print(f".{t}")
