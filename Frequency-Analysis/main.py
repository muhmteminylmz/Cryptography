def caesar_encrypt(plain_text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    for ch in plain_text:
        if ch.lower() in alphabet:
            
            index = alphabet.index(ch.lower())
            shifted_index = (index + shift) % len(alphabet)
            encrypted_ch = alphabet[shifted_index]

            if ch.islower():
                encrypted_text += encrypted_ch
            else:
                encrypted_text += encrypted_ch.upper()

        else:
            encrypted_text += ch
    print(encrypted_text)
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_text = ""

    for ch in ciphertext:
        if ch.lower() in alphabet:
            
            index = alphabet.index(ch.lower())
            shifted_index = (index - shift) % len(alphabet)
            decrypted_ch = alphabet[shifted_index]

            if ch.islower():
                decrypted_text += decrypted_ch
            else:
                decrypted_text += decrypted_ch.upper()

        else:
            decrypted_text += ch

    return decrypted_text

plain_text = "Bugun arabami yikamaya gidiyorum"
shift = 3

encrypted_text = caesar_encrypt(plain_text, shift)

decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Gercek Metin: ", plain_text)
print("Sifreli Metin: ", encrypted_text)
print("Cozulen Metin: ", decrypted_text)

"""
def caesar_decrypt_frequencies(ciphertext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_text = ""

    for ch in ciphertext:
        if ch.lower() in alphabet:
            index = alphabet.index(ch.lower())
            shifted_index = (index - shift) % len(alphabet)
            decrypted_ch = alphabet[shifted_index]

            if ch.islower():
                decrypted_text += decrypted_ch
            else:
                decrypted_text += decrypted_ch.upper()
        else:
            decrypted_text += ch

    return decrypted_text

# Şifreli metin
ciphertext = "Exkqv jxlwvkz ldyvneoxv vjyfpg"
# Türkçe için olası en sık harflerden biri 'e' olduğunu kabul edebiliriz.
# Türkçe'de 'e' harfi sıkça kullanılır, ancak farklı dillerde farklı olabilir.

# Frekans analizi yapalım
freqs = frequency_analysis(ciphertext)
print("Harf Frekansları: ", freqs)

# Türkçe metinlerde en sık kullanılan harflerin 'e' olduğunu varsayalım
# Burada 'e' harfi genellikle en sık kullanılan harf olduğundan, ona denk gelen şifreli harfi kullanacağız.
most_common_letter = 'e'

# En yaygın harfi çözmek için
# Eğer şifredeki en yaygın harf 'k' ise, kaydırmayı bulmak için:
shift = ord('k') - ord(most_common_letter)
print(f"En yaygın harf 'k' olduğunda kaydırma: {shift}")

# Şifreyi çözmek için bu kaydırmayı kullanarak
decrypted_text = caesar_decrypt_frequencies(ciphertext, shift)
"""