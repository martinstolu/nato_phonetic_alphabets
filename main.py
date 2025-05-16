import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dic = {row.letter:row.code for (index, row) in nato_data.iterrows()}

user_input_digits = True
while user_input_digits:

    user_input= input("Enter a word: ").upper()
    try:
        word_to_print =[new_dic[letter] for letter in user_input]
    except KeyError:
        print("sorry, only letters in the alphabet please.")
    else:
        print(word_to_print)
        user_input_digits = False
