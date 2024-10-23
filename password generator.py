import random
letters=["a", "b", "c", "d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
         "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","#","$","%","&",'(",")',"*","+"]

print("Welcome To Password Generator!")

n_letter=int(input("How many letters you want in your password?"))
n_numbers=int(input("How many numbers you want in your password?"))
n_symbols=int(input("How many symbols you want in your password?"))

password=[]
for i in range(1,n_letter+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
random.shuffle(password)
re_password=""
for i in password:
    re_password+=i
    print(re_password)

