import pandas as pd

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# {new_key:new_value for (index, row) in df.iterrows()}

with open("nato_phonetic_alphabet.csv") as file:
    data = pd.read_csv(file)
    phonetic_alphabet_dict = {row.}
    
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
