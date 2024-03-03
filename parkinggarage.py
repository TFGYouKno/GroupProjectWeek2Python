class Parking_Garage():
    '''
    Welcome to Fcuklechuck's Parking Garage!
    '''
    def __init__(self, peasant_tickets = 21, premium_tickets = 11, peasant_parking_spaces = 21, premium_parking_spaces = 11):
        self.peasant_tickets = list(range(1, 21))
        self.premium_tickets = list(range(1, 11))
        self.peasant_parking_spaces = list(range(1,21))
        self.premium_parking_spaces = list(range(1,11))
        self.current_ticket = {"paid": "not paid"}

    def take_ticket(self):
        ticket_type = input(f'welcome to Fcuklechucks Parking! Would you like $70 peasant parking or $120 premium parking?')
        if ticket_type.lower() == "peasant parking":
            if not self.peasant_tickets:
                print("We're full up! Kick rocks, ya bum!")
            suckers_choice = int(input(f'available peasant spaces{self.peasant_parking_spaces} choose a space, peasant!'))         
            if suckers_choice in self.peasant_parking_spaces:
                self.peasant_tickets.remove(suckers_choice)
                self.peasant_parking_spaces.remove(suckers_choice)
                print("You successfully picked a spot. You are good at life!")
            else:
                print('Another peasant is occupying this space. Choose another to infest with your presence!')
        elif ticket_type.lower() == "premium parking":
            if not self.premium_tickets:
                print("We're full up! Kick rocks, you slightly wealthier bum!")
            premium_suckers_choice = int(input(f'Available premium spaces{self.premium_parking_spaces} choose your space, my liege!'))
            if premium_suckers_choice in self.premium_parking_spaces:
                self.premium_tickets.remove(premium_suckers_choice)
                self.premium_parking_spaces.remove(premium_suckers_choice)
                print("Excellent choice, Boss!")
            else:
                print("My sincerest apologies, Sir and/or Madam, that premium space is already taken! Please choose another?")
        else:
            print("Invalid entry. You are not very good at this are you?")

    def pay_for_Parking(self):
        ticket_type_exit = input(f'We are sooooooo sorry to see you go... could have parted out that rust bucket for beer money. Anyway, peasant or premium?')
        if ticket_type_exit.lower() == "peasant":
            
            payment = float(input("Please give us your money!"))
            if payment >= 70:
                print("Thanks for the money! Would you like to pay an additional $50 to get your hubcaps and catalytic converter back?")
                self.current_ticket["paid"] = True
            else:
                print("You have been deemed financially unfit for vehicle ownership. Your car has been siezed by Fcuklechucks parking. Come back when you have my money! Or did you forget how to count? Or your social class?")
                self.current_ticket["paid"] = False
        if ticket_type_exit.lower() == "premium":
            payment = float(input("Please give us your money!"))
            if payment >= 120:
                print("Thanks for the money! As a courtesy, we have returned your hubcaps, change, and catalytic converter to your back seat. Have a nice day!")
                self.current_ticket["paid"] = True
            else:
                print("You really opted for Premium, while being financially unfit for vehicle ownership? Pshhh. Your car has been siezed by Fcuklechucks parking. Come back when you have my money! Or did you forget how to count? Or your social class?")
                self.current_ticket["paid"] = False
        self.leave_Fcuklechucks()
    def leave_Fcuklechucks(self):
        if self.current_ticket["paid"] == True:
            print("Thanks for choosing Fcuklechucks! We hope you enjoyed your stay as much as we enjoy your money. Dont let the door hit you in the ass on the way out, and please rate five stars on Yelp!")
        else:
            self.pay_for_Parking()

    def runner(self):
        while True:
            check_point = input("Are you coming or going? ").lower()
            if check_point == "coming":
                self.take_ticket()
            elif check_point == "going":
                self.pay_for_Parking()
                break
            else:
                print("Dude, it is not rocket surgery. In or out, Dishpit.")
user = Parking_Garage()
user.runner()