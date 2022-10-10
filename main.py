import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

user_input = input("Enter a word: ").upper()
# getting csv file with pandas and converting rows with the name of each row to a dictionary
nato_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
# creating a list to match the letters of the user_input
nato_list = [nato_dict[letter] for letter in user_input]
print(nato_list)

