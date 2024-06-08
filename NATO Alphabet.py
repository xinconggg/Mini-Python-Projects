import pandas

# Create a Dataframe then a Dictionary:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter : row.code for (index,row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
<<<<<<< HEAD
print(output_list)
=======
print(output_list)
>>>>>>> afa1b6d4c7400ab9be23497e17a7a62814c9c8b3
