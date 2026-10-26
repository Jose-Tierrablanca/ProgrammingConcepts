#Importing the Regular Expression module
import re

#defining the main function that splits the paragraph into sentences
def main():
    """
    The main function of the program that receives user input and uses a
    random expression method to separate by sentence and stores each
    sentence in a list.

    Parameters:
        None

    Variables:
        paragraph (str): User input for paragraph analyzer
        pat (str): The pattern used to define a sentence
        split_sentences (list): A list of sentences separated

    Logic:
        1. Receive user input (paragraph expected)
        2. Split the paragraph into sentences
        3. Store all the sentences in a list
        4. Send the list to the next function

    :return:
    None
    """
    #Sets the paragraph and pattern used for the re.findall method
    paragraph = input("Enter a paragraph: ")
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    #Using the specified pattern, the findall method checks for periods
    #Then checks beyond it to truly find out if it really is a sentence
    split_sentences = re.findall(pat, paragraph, flags=re.DOTALL | re.MULTILINE)

    #Sends the list made onto the following function
    paragraph_analyzer(split_sentences)

    #The list of sentences is counted and printed one by one
def paragraph_analyzer(sentence):
    """
    The function that counts the number of sentences stored in the list
    Prints every sentence from the list one by one

    Parameters:
        sentence (list): A list of sentences

    Variables:
        number_of_sentences (int): The number of sentences stored in the list

    Logic:
        1. Receive the list of separated sentences
        2. Count and print the number of sentences stored in the list
        3. Print every sentence in the list

    :return:
    None
    """
    #Uses len() to display the amount of sentences in the paragraph
    number_of_sentences = len(sentence)
    print("Number of sentences: ", number_of_sentences)

    #Uses a for-loop to print every categorized sentence
    for i in sentence:
        print(i)

if __name__ == "__main__":
    main()