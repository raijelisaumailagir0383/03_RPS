# checks user enters rock / paper / scissors
def rps_checker():

    valid = False
    while not valid:
        response = input("Choose: ").lower()

        if response == "r" or response == "rock":
            return "rock"
        elif response == "s" or response == "scissors":
            return "scissors"
        elif response == "s" or response == "scissors":
            return "scissors"
        else:
            print("Please enter rock  / paper / scissors ")

user_choice = rps_checker()
print(user_choice)
valid = False

while not valid:
    response = rps_checker()
    print(response)

