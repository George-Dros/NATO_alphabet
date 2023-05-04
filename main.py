import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter:row.code for (index, row) in data.iterrows()}


word = input("Word: ").upper()
output_list = [dictionary[letter] for letter in word]

print(output_list)

