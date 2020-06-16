# checks user enters rock / paper / scissors
def rps_checker():

    valid = False
    while not valid:
        # ask user to choose and puts their answer into lowercase
        response = input("Choose: ").lower()

         # checks user response and either returns it or ask question again
        if response == "r" or response == "rock":
           return "rock"
        elif response == "s" or response == "scissors":
              return "scissprs"
        elif response == "p" or response == "paper":
            return "paper"
        else:
            print("Please enter rock/ paper/ scissors ")

# **** main routine *****

    while not valid:
       response = rps_checker()
    print(response)













