with open('file.txt', 'r') as f:
    print(f.read())
    f.seek(6)
    current = f.tell()
    print(current)
    data = f.read()
    print(data)
with open('simple.txt', 'w') as f:
    f.write("hello word ")
    f.truncate(5)
with open('simple.txt', 'r') as f:
    print(f.read())

