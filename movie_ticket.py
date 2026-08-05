ticket_price = int(input("Enter ticket price : "))
age = int(input("enter persons age : "))
student = input("enter y if your are student otherwise n : ").strip().lower()

if age < 10 or age >60 :
    ticket_price = ticket_price - (ticket_price * 50 /100)
    print(f"Movie ticket price will be  : {ticket_price}")
elif student == 'y':
    ticket_price = ticket_price - (ticket_price * 25 /100)
    print(f"Movie ticket price will be  : {ticket_price}")   
else:
    print(f"Movie ticket price will be  : {ticket_price}")