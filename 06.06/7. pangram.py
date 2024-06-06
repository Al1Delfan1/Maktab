def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True

input_string = "The quick brown fox jumps over the lazy dog"

output = is_pangram(input_string)
print(output)
