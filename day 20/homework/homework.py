
letters = ['a', 'b', 'c', 'e', 'f', 'i', 'j', 'o', 'u']
vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0
for letter in letters:
    if letter in vowels:
        vowel_count += 1

print(f"ხმოვნების რაოდენობა: {vowel_count}")
