
#Accumulator for the amount of buyers (int)
buyers = 0

def main():
    """
    The main function of the program handling the flow of data input
    Holds a loop calling the other functions while keeping count of buyers

    Parameters:
        None

    Variables:
        tickets_available (int): The number of tickets available
        tickets_bought (int): The number of tickets bought

    Logic:
        For every iteration:
        1. Call the prompt function
        2. Set tickets_bought by calling the ticket_selection function
        3. Subtract the return value of ticket_selection from tickets_available
        4. Increase buyers
        5. Print a final message and total buyers when all tickets are sold

    :return:
        None
    """

    #Allow modifications to buyer
    global buyers
    tickets_available = 10
    #Repeats until all tickets have been sold
    while tickets_available > 0:
        #Passing tickets available to the f-strings in the print functions
        prompt(tickets_available)
        #Calls the function to determine how much will be subtracted
        #A new value for every iteration
        tickets_bought = ticket_selection(tickets_available)
        #Subtracts the amount bought from total tickets
        tickets_available -= tickets_bought
        #Increase the running total
        buyers += 1
        #Creates an empty space, aids me in reading
        print()
    #Displays a final message and the running total
    print("All tickets have been sold!")
    print(f"The last 20 tickets were bought by {buyers} different customers")

def prompt(ticket_number):
    """
    Displays different messages depending on how many tickets can be sold

    Parameters:
        ticket_number (int): The number of tickets left

    Variables:
        None

    Logic:
        1. If the amount is over what can be bought, give the max value
        2. If there is only 1 ticket available, let it be known
        3. If there is between 2 and 4, change the prompt

    :return:
        None
    """

    #If statement to handle which message to display
    #Based on the amount of tickets passed through the parameter
    if ticket_number >= 4:
        print(f'There are only {ticket_number} tickets available')
        print('The max amount of tickets per buyer is 4')
    elif ticket_number == 1:
        print('There is only 1 ticket available, will you buy it?')
    else:
        print(f'There are only {ticket_number} tickets available')
        print('You can buy some or all')

def ticket_selection(remaining):
    """
    Handles the input for how many tickets are bought for that iteration
    Uses many if statements to handle maximums

    Parameters:
        remaining (int): The number of tickets remaining

    Variables:
        validity (str): 'valid' or 'invalid'
        choice (str): 'Y' and 'y' or anything else
        current purchase (int): The number of tickets bought in that iteration

    :return:
        Current purchase (int): The number of tickets bought in that iteration
    """
    #Under a certain circumstance, we may have to modify the running total
    global buyers

    #Resets the validity variable so the logic can be checked every iteration
    validity = 'invalid'
    #Prompt for when the tickets left is not 1
    if remaining > 1:
        print('How many tickets would you like to purchase?')
    else: validity = 'valid'
    #Only activates when the tickets left is only 1
    if validity == 'valid':
        choice = input('(y/n) ')
        #Allows any input but does not end the program
        #Until the input is either 'y' or 'Y'
        if choice == 'y' or choice == 'Y':
            current_purchase = 1
        else:
            #If a buyer chooses to not buy, then program goes to the next iteration
            #Each iteration increases the running total but "buyers -= 1"
            #Cancels it out
            print('Alright')
            buyers -= 1
            current_purchase = 0
    #If the previous conditions have not been met, a loop will happen
    #Looped until a 'valid' integer is given
    while validity == 'invalid':
        #try-except block to only accept integers
        try:
            #More formatting depending on the tickets available
            if remaining > 4:
                current_purchase = int(input('(1-4): '))
            else: current_purchase = int(input(f'(1-{remaining}): '))
            #If both conditions are not met, the while block loops
            #Ex. Prevents 3 from being bought when only 2 are available
            if current_purchase in range(1, 5) and current_purchase in range(1, remaining + 1):
                validity = 'valid'
            else:
                print()
                print('You have not entered an allowed number of tickets')
                print('Try again')
        #ValueError exception to not crash over non-integer inputs
        except ValueError:
            print()
            print('Please enter an integer between 1 and 4')
    #Value returned for the subtraction of available tickets
    return current_purchase

#Calling the main function
if __name__ == '__main__':
    main()