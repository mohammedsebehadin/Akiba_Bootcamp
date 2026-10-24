sentence = "python is useful and python is powerful"

def clear_text(sentence):
    lowered = sentence.lower()
    return "".join(
        char for char in lowered
        if char.isalnum() or char.isspace()
    )

def count_characters(sentence):
    return len(sentence.strip())

def count_words(sentence):
    return len(sentence.split())

def vowel_consonant(sentence):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in sentence.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

                return vowel_count, consonant_count

def longest_word(sentence):
    return max(sentence.split(), key=len, default="")

print("Cleared text:", clear_text(sentence))
print("Character count:", count_characters(sentence))
print("Word count:", count_words(sentence))
print("Vowels and consonants:", vowel_consonant(sentence))
print("Longest word:", longest_word(sentence))
