#Asks for the name of expenses and their costs and returns
#The cheapest and most expensive expenses and the total expenses
#Using the reduce function

#Allows the use of .reduce(function, list)
import functools


#Bulk of the code
def main():
    """
    The main function calling other functions to handle the
    Input collection and result output
    While also storing the data in a dictionary and list

    Parameters:
    None

    Variables:
    expenses_dictionary (dictionary): Dictionary of expenses
    expenses_list (list): List of expenses (cost)
    answer (boolean): True or False
    success (boolean): True or False
    more (string): 'y' or 'n'
    expense_summation (float): Sum of all your expenses
    highest_value (float): Highest expense
    lowest_value (float): Lowest expense

    Logic:
    1. Create an empty dictionary and an empty list
    2. Loop obtaining names and values
    3. Ask if more expenses are added
    4. Copy the dictionaries' values to the list
    5. Run the .reduce functions
    6. Send the data for formatting of the results

    :return: None
    """

    #Creates both an empty dictionary and an empty list for later use
    expenses_dictionary = {}
    expenses_list = []

    #The condition to begin the while loop
    answer = True

    #Looping to ask if there are more expenses to be entered
    #Nested if block to ask for input
    #The last 2 lines confirm iteration
    while answer:
        #asks_expenses is called to handle user input
        success = ask_expenses(expenses_dictionary)
        if success == False:
            more = input('Do you want to continue adding expenses? (y/n) ')
        else:
            more = input('Do you want to add another expense? (y/n): ')
        more = more.lower()
        answer = more.startswith('y')

    #Copies the values of the expenses onto a list
    for i in expenses_dictionary:
        expenses_list.append(expenses_dictionary[i])

    #Uses the copied list to use the reduce mini functions
    expense_summation = functools.reduce(adding, expenses_list)
    highest_value = functools.reduce(find_highest, expenses_list)
    lowest_value = functools.reduce(find_lowest, expenses_list)

    #Calls the function that will format the results
    format_results(expenses_dictionary, expense_summation, highest_value, lowest_value)


#Handles user input
def ask_expenses(dictionary_entry):
    """
    This function handles the input for dictionary keys
    And makes sure that there are no duplicates and that
    The values are all floats

    Parameters:
    dictionary_entry (dictionary): Dictionary of expenses

    Variables:
    expenses_name_raw (string): Raw expenses name
    expenses_name_undercooked (string): Expenses name but lowercase
    expenses_name (string): Expenses name without any tailing spaces
    dictionary_entry (dictionary): Dictionary of expenses
    expense_value (float): Expenses value

    Logic:
    1. Receive an input as a string
    2. Normalize the results to lowercase
    3. Remove any whitespaces so that repetition of keys are not accepted
    4. Checks repetition
    5. Accepts only valid values
    6. Appends the inputs to the dictionary

    :return: None
    """

    #Formats user input so that all the keys are in lowercase
    expenses_name_raw = input('What is the name of the expense? ')
    expenses_name_undercooked = expenses_name_raw.lower()
    expenses_name = expenses_name_undercooked.strip()

    #Checks for repeated expenses
    if expenses_name in dictionary_entry:
        print('You have already entered an expense of that name')
        return False

    #Handles entry of numbers
    #If valid, it adds the expense name and cost to the dictionary
    #If invalid, it will prompt reentry
    while True:
        try:
            expense_value = float(input('What is the value of the expense? '))
            dictionary_entry[expenses_name] = expense_value
            return True
        except ValueError:
            print('Only numbers are allowed, please try again')

#The next 3 functions are for use in .reduce(function, list)
def adding(a, b):
    """
    Adds two numbers

    Parameters:
    a (float): First number
    b (float): Second number

    Logic:
    Add two numbers

    :return: a + b
    """
    return a + b

def find_highest(a, b):
    """
    Find the highest value in the list

    Parameters:
    a (float): First number
    b (float): Second number

    Logic:
    Find the highest value in the list

    :return: max(a, b)
    """
    return max(a, b)

def find_lowest(a, b):
    """
    Find the lowest value in the list

    Parameters:
    a (float): First number
    b (float): Second number

    Logic:
    Find the lowest value in the list

    :return: min(a, b)
    """
    return min(a, b)

#Makes the results all pretty
def format_results(expenses_dict, expense_summation, highest_value, lowest_value):
    """
    Format the results for printing

    Parameters:
    expenses_dict (dictionary): Dictionary of expenses
    expense_summation (float): Expenses summation
    highest_value (float): Highest expense
    lowest_value (float): Lowest expense

    Variables:
    high_value (list): Highest expense
    highest_value (list): Highest expense
    lowest_value (list): Lowest expense
    lowest_value (list): Lowest expense

    Logic:
    1. Obtain the expenses summation and print
    2. If there is more than 1 highest or lowest expense
       List them as such, if not just print the highest
       or lowest expense

    :return: None
    """

    #Print the total expenses
    print(f'The sum of all your expenses is ${expense_summation:.2f}')

    #Find highest cost expense(s)
    high_value = []
    for i in expenses_dict:
        if expenses_dict[i] == highest_value:
            high_value.append(i)
    if len(high_value) == 1:
        print(f'The highest value is {high_value[0]} for ${highest_value:.2f}')
    else:
        print(f'The highest expenses (${highest_value:.2f}) are:')
        for i in high_value:
            print(i)


    #Find lowest cost expense(s)
    low_value = []
    for i in expenses_dict:
        if expenses_dict[i] == lowest_value:
            low_value.append(i)
    if len(low_value) == 1:
        print(f'The lowest value is {low_value[0]} for ${lowest_value:.2f}')
    else:
        print(f'The lowest expenses (${lowest_value:.2f})are:')
        for i in low_value:
            print(i)

if __name__ == '__main__':
    main()