filename='learnpython.txt'

with open(filename) as file:
    lines=file.readlines()
    


fileread=''
for line in lines:
    fileread +=line.rstrip()
    
change=fileread.replace('Python','Java')
print(change)

