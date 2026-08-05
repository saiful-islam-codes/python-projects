import random
computer = random.randint(1 , 100)

while True : 
    user = int(input("Enter your number ( 1 - 100) :"))
    
    if user == computer:
        print("got it!")
        break
    elif(user > computer):
        print("Too high..")
        break
    elif(user < computer):
        print("Too low!!!")
        break
    else:
        print("invalid..")        
        break        

