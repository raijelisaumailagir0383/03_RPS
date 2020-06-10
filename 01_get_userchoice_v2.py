# checks user enters rock / paper / scissors
def rps_checker():

    valid = False
    while not valid:
        # asks user to choose and puts their answer into lowercase
        response = input("Choose: ").lower()

        # checks user response and either returns it or asks question again
        if response == "r" or response == "rock":
            return "rock"
        elif response == "s":
            return "scissors"
        elif response == "p":
            return "paper"
        else:
            print("Please enter 'rock, paper or scissors'")

# **** main routine *****

user_choice = rps_checker()
print(user_choice)
