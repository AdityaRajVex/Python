# Name: Aditya Raj
# File Name: AdityaRaj_quiz2.py
# Date: 11/30/2023
#
# Short Description: Create the word game Scrabble
# Program description output
print('This program is a word game called Scrabble. When you enter a word, the value of the word will be calculated for you.\n')
# Initialize the data
tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }
# Calculations
points = 0
user_input = input('Enter a word: ')
for i in user_input:
    for x in tile_dict:
        if i == x:
            points += tile_dict[x]

print(f'\n"{user_input}" is worth {points} points')

# Display results
'''
testing run data
Trial 1:
    This program is a word game called Scrabble. When you enter a word, the value of the word will be calculated for you.
    
    Enter a word: PYTHON
    
    "PYTHON" is worth 14 points
    
    Process finished with exit code 0

Trial 2:
    
    Enter a word: HELLO WORLD!
    
    "HELLO WORLD!" is worth 17 points
    
    Process finished with exit code 0

'''
