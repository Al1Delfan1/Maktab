input_string = input("Enter a string: ")

words = []
current_word = []

for char in input_string:
    if char.isupper() and current_word:
        words.append(''.join(current_word))
        current_word = [char]
    else:
        current_word.append(char)

words.append(''.join(current_word))

output_sentence = ' '.join(words)

print(output_sentence)
