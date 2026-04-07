import random
letters =["A","a","B","b","C","c","D","d","E","e","F","f","G","g",
          "H","h","I","i","J","j","K","k","L","l","M","m","N","n",
          "O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v",
          "W","w","X","x","Y","y","Z","z",]

numbers = ["1","2","3","4","5","6","7","8","9","0",]

char = ["@","!","%","$","#","*","&","/","=","+","-",]

num = int(input("how much number do you like in your password ? "))
cha = int(input("how much charector do you like in your password ? "))
let = int(input("how many letters do youlike in your password ? "))
password =[]
for x in range(1,num+1):
 
 password+= random.choice(numbers)

for f in range(1,cha+1):
  password+= random.choice(char)

for k in range(1,let+1):
 password+= random.choice(letters)


random.shuffle(password)

password = "".join(password)


print(f"your password is {password}")