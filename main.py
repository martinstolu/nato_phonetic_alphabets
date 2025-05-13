import pandas

user_input= input("Write a word: ").upper()
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dic = {row.letter:row.code for (index, row) in nato_data.iterrows()}
word_to_print =[new_dic[letter] for letter in user_input]
print(word_to_print)
