import os
keyword = input()
file_with_key = []
for path, dirs, files in os.walk("D:\/"):
    for file in files:
        with open(f"{path}\{file}", encoding="utf-8") as f:
            if keyword in f.read():
                file_with_key.append(file)

print(file_with_key)
