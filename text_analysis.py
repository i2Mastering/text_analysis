"""
Module for processing user input, identifying vowels, extracting unique words, and determining the three largest words in a sentence.

This script prompts the user to enter a detailed sentence (minimum 10 words), then performs the following operations:
- Counts the vowels in the sentence.
- Identifies unique words, ignoring case.
- Extracts the three largest words and their character counts.

Classes:
    - stringFunctions: Handles user input.
    - vowelFunction: Counts and displays vowels.
    - uniqueWords: Extracts unique words.
    - maxChar: Identifies the three longest words.

Example Usage:
    $ python text_analysis.py
    Hello there, please tell me how your day has been...
    The total amount of vowels in your sentence is 15...
    The unique words used in your sentence are: [...]
    The 3 largest words in your sentence are [...]

Author: Ike Iloegbu
License: MIT
"""

# List of vowels for reference
vowels = 'AaEeIiOoUu'

class stringFunctions:
    """
    Handles user input, ensuring a minimum of 10 words.
    """
    @staticmethod
    def userPrompt():
        """
        Prompts the user for input and validates that the sentence contains more than 10 words.

        Returns:
            str: The user's input string.
        """
        while True:
            global userInput
            userInput = input("Hello there, please tell me how your day has been (more than 10 words): \n")
            if len(userInput.split()) <= 10:
                print("Your response is too short. Please try again.")
            else:
                print(f"\nYou said: {userInput}\n")
                print(f"Thanks for sharing! You used {len(userInput.split())} words.")
                break
        return userInput
    
    stringToList = list(userPrompt())

class vowelFunction:
    """
    Counts vowels in the user's input string.
    """
    @staticmethod
    def vowelCounter():
        """
        Identifies vowels in the input string and prints their count.
        """
        vowelCheck = [char for char in stringFunctions.stringToList if char in vowels]
        print(f"\nThe total amount of vowels in your sentence is {len(vowelCheck)}.")
        print(f"The vowels in your sentence: {sorted(set(vowelCheck))}")

vowelFunction.vowelCounter()

class uniqueWords:
    """
    Identifies unique words from the input string, ignoring case and punctuation.
    """
    userInput = userInput.strip('.')
    userInput = userInput.lower()
    wordList = []
    for word in userInput.split():
        if word not in wordList:
            wordList.append(word)
    
    print(f"\nThe unique words used in your sentence are: {wordList}")

class maxChar:
    """
    Identifies the three longest words in the sentence and their character count.
    """
    @staticmethod
    def charOrder():
        """
        Finds the three largest words in the input and prints their lengths.
        """
        wordsInList = userInput.split()
        wordSort = sorted(wordsInList, key=len, reverse=True)
        wordCount = [len(word) for word in wordSort]
        print(f"\nThe 3 largest words in your sentence are {wordSort[:1]} ({wordCount[:1]} characters), {wordSort[1:2]} ({wordCount[1:2]} characters), and {wordSort[2:3]} ({wordCount[2:3]} characters).")

maxChar.charOrder()

print("\nTake care. Adios!")
        
    
        
    
            
                
    

       


        
        



    
   

