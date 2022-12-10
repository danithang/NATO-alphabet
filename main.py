import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# getting csv file with pandas and converting rows with the name of each row to a dictionary
nato_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}


# defining a function for the keyerror and using a while loop to continue until user gives proper input
def generate_phonetic():
    error_key = True
    while error_key:
        user_input = input("Enter a word: ").upper()
        try:
            # creating a list to match the letters of the user_input
            nato_list = [nato_dict[letter] for letter in user_input]
        except KeyError:
            print("Sorry, please use only letters!")
        else:
            error_key = False
            print(nato_list)


generate_phonetic()
