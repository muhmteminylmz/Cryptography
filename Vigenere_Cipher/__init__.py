import itertools as it

class vigenere:
    def __init__(self,word,key):
        self.letter_to_number = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        self.encrypted_word = list()
        self.key = key.lower()
        self.key = it.cycle(key)
        self.word = word.lower()
        self.word = list(word)
    def algorithm(self):
        for letter in self.word:
            key_letter = next(self.key)
            encrypted_value = self.getAddOfLetterValues(letter,key_letter)%26
            self.encrypted_word.append(chr(encrypted_value + ord('a')))
        return ''.join(self.encrypted_word)
    def getAddOfLetterValues(self,letter_word,key_word):
        return self.letter_to_number.get(letter_word) + self.letter_to_number.get(key_word)



word = input("Lutfen kelimeyi giriniz: ")
key = input("Lutfen anahtari giriniz: ")

obj = vigenere(word,key)

print(obj.algorithm())