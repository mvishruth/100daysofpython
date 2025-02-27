import pandas as pd

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv") as file:
    data = pd.read_csv(file)
    phonetic_alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}
    
    
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word:").upper()
output_list = [phonetic_alphabet_dict[letter] for letter in word]
print(output_list)
