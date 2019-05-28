def catdog(petname):
    try:
        with open(petname) as name:
            pet=name.read()
    except FileNotFoundError:
        pass
    else:
        print(pet)
        
pet=['cats.txt','dog.txt']              #10.8 10.9已完成

for petname in pet:
    catdog(petname)
