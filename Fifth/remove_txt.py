import os

files=os.listdir('Fifth/')

names=[file.replace('.txt', '') for file in files]

print(names)

for index in range(len(files)):
    os.rename('Fifth/'+ files[index],'Fifth/'+ names[index])
