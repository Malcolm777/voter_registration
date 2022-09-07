




"Python Voter Registration Application"
# first exercise produces a voter registration application asking the user
# a few simple questions followed by a confirmation of registration
# provided the user is eligible. The
# second part documents your testing and Pylint analysis results
# The application will prompt the user for:
# first name, last name, age, country of citizenship, state of residence and
# zipcode

# continue_program


import sys


def continue_program():
    '''
    prompts user to continue program
    '''
    choice = input("Do you want to continue with voter registration?\n")
    if choice in ('yes', 'Yes', 'YES'):
        return True
    if choice in ('No', 'NO', 'no'):
        return sys.exit('Thank you for using the Python Voter Registration Application')


def error_check(string):
    '''
    error check
    checks string to verify each char is letter
    '''
    if string.isalpha():
        return True
    return False


def get_name(name_string):
    '''
    gets the name from the user
    if user input is valid, it will return name
    '''
    while True:
        if not continue_program():
            return "Exit"
        name = input(name_string)
        if error_check(name):
            return name


def get_age():
    '''
    asks user for an age
    checks age range
    '''
    while True:
        if not continue_program():
            return -1
        try:
            name = input("What is your age?\n")
            age = int(name)
            if age < 18:
                name = input("Are you 18 years of age?\n")
                name = name.lower()
                if name == "no":
                    print("You must be 18 or older to vote.")
                    return -1
            elif 120 >= age >= 18:
                return age
            elif age > 120:
                print("Please enter a valid age.")
            elif age < 18:
                print("You must be 18 or older to vote.")
            else:
                print("You must enter a valid number. ")
        except ValueError:
            pass


def get_country():
    '''
    prompts user to enter country
    '''
    while True:
        if not continue_program():
            return "Exit"
        choice = input("Are you a U.S. citizen?\n")
        choice = choice.lower()
        if choice in ('yes' or 'Yes' or 'YES'):
            return "yes"
        if choice == "no":
            print("You must be a U.S. citizen to vote.")


def get_state():
    '''
    prompts user for home state
    accepts only 2 letter entries
    '''
    while True:
        if not continue_program():
            return "Exit"
        state = input("What state do you live?\n")
        if error_check(state):
            state = state.lower()
            if len(state) == 2:
                return state
            if len(state) != 2:
                print("Length of state must be two letters.")
            else:
                break


def get_zip():
    '''
    gets zip code
    must be 5 integers
    returns the zipcode
    '''
    while True:
        if not continue_program():
            return -1

        try:
            zip_code = input("What is your zipcode?\n")
            if len(zip_code) == 5:
                return int(zip_code)
            if len(zip_code) != 5:
                print("Please enter a 5 digit zip code.")
        except ValueError:
            pass


if __name__ == '__main__':
    # Welcome message
    print("***************************************************************************")
    print("Welcome to the Python Voter Registration Application!\n")

    # array to store voter values
    VOTER = []
    while True:

        # get first name
        FNAME = get_name("What is your first name?\n")
        VOTER.append(FNAME)

        # get last name
        LNAME = get_name("What is your last name?\n")
        VOTER.append(LNAME)

        # get age
        AGE = get_age()
        VOTER.append(AGE)

        # get country
        COUNTRY = get_country()
        VOTER.append("YES")

        # get state
        STATE = get_state()
        VOTER.append(STATE.upper())

        # get zip code
        ZIP = get_zip()
        VOTER.append(ZIP)

        if len(VOTER) == 6:

            print()
            print("Thanks for registering to vote. Here is the information we received:")
            print("Name (first last): ", VOTER[0], VOTER[1])
            print("Age:", VOTER[2])
            print("U.S. Citizen:", VOTER[3])
            print("State: ", VOTER[4])
            print("Zip Code: ", VOTER[5])
            print("Thanks for trying the voter registration application.")
            print("Your voter registration card should be shipped within 3 weeks.")
            sys.exit(
                "***************************************************************************\n")
