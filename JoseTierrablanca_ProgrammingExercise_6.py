#Importing the regular expression module to run the re.match functions
import re

#Main function that displays the prompts for the inputs
#Calls all the other functions for verification of the inputs
def main():
    """
    Asks the user to enter a phone number, a social security, and a zip code.
    Calls functions passing each of the variables for their verification.

    Parameters:
    None

    Variables:
    phone_number (str): phone number entered by the user
    social_security (str): social security entered by the user
    zip_code (str): zip code entered by the user

    Logic:
    1. Ask for the user to enter the numbers for each variable
    2. Pass through their respective functions for verification

    :return:
    None
    """

    #Starter prompt
    print("Please enter the following information:")

    #Asks for all the information in 3 different inputs
    phone_number = input('Phone number: ')
    social_security = input('Social security: ')
    zip_code = input('Zip code: ')

    #Calls all the functions passing their respective arguments
    print('')
    verify_phone_number(phone_number)
    verify_social_security(social_security)
    verify_zip_code(zip_code)

#Function verifying the phone number
def verify_phone_number(number):
    """
    Verifies if the entered phone number is a valid phone number through pattern checking

    Parameters:
    number (str): phone number entered by the user

    Variables:
    number (str): phone number entered by the user

    Logic:
    Check if the entered phone number is a valid phone number through pattern checking
    1. Checks for usage of parentheses around the area code part
    2. Checks for usage of dashes to separate the groups

    :return:
    None
    """

    #If loop to display whether the input matches the pattern
    #Accepts (123) 456 - 7890, 123 456 7890, and 123 - 456 - 7890
    if re.match(r'^(\(\d{3}\)\s|\d{3}[ -])\d{3}[ -]\d{4}$', number):
        print("Phone number is valid")
    else: print("Phone number is not valid")

#Function verifying the social security
def verify_social_security(social):
    """
    Verifies if the entered social security is a valid social security through pattern checking

    Parameters:
    social (str): social security entered by the user

    Variables:
    social (str): social security entered by the user

    Logic:
    Check if the entered social security is a valid social security through pattern checking
    1. Checks for usage of spaces or dashes to separate the groups

    :return:
    None
    """

    #If loop to display whether the input matches the pattern
    #Accepts 123 45 6789 and 123 - 45 - 6789
    if re.match(r'^\d{3}[ -]\d{2}[ -]\d{4}$', social):
        print("Social security is valid")
    else: print("Social security is not valid")

#Function verifying the zip code
def verify_zip_code(zip):
    """
    Verifies if the entered zip code is a valid zip code through pattern checking

    Parameters:
    zip (str): zip code entered by the user

    Variables:
    zip (str): zip code entered by the user

    Logic:
    Check if the entered zip code is a valid zip code through pattern checking
    1. Checks whether the zipcode is a 5-digit or the extended 9-digit zip code

    :return:
    None
    """

    #If loop to display whether the input matches the pattern
    #Accepts 12345 and 12345-6789
    if re.match(r'^\d{5}(-\d{4})?$', zip):
        print("Zip code is valid")
    else: print("Zip code is not valid")

if __name__ == '__main__':
    main()