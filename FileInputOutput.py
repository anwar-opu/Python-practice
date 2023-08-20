# FILE READ :

# f = open('newfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# FILE WRITE :

# f =open('newfile.txt', 'w')
# text = f.write(' hello world')
# f.close()

# ADD TEXT file:

f =open('newfile.txt', 'a')
text = f.write(' world')
f.close()

with open('newfile.txt', 'a') as f :
    f.write(' welcome')