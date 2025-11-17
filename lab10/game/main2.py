import re

with open("mockdata.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

names = []
surnames = []
types = []

for line in lines:
    parts = line.strip().split("\t")
    if len(parts) < 4:
        continue
    name = parts[0]
    surname = parts[1]
    
    match = re.search(r"\.(\w+)$", parts[3])
    if match:
        ext = match.group(1)
    else:
        ext = ""
    
    names.append(name)
    surnames.append(surname)
    types.append(ext)

with open("name.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(names))

with open("surname.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(surnames))

with open("typeFile.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(types))

print("Файлы успешно созданы!")