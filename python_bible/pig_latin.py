#get sentence from user
original = input("Please enter the Sentence: ").strip().lower()

# split sentence into words
words = original.split()

#loop through the words and convert to pig latin
new_words = []
#if it starts with vowels, add "yay"
#otherwise, move the first consonant cluster to end and add "ay"

for word in words :
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break #goes to the else statement
        consonants = word[:vowel_pos]
        new_word = word[vowel_pos:] + consonants + "ay"
        new_words.append(new_word)

#stick words into sentence
new_sentence = " ".join(new_words)

#output the final string
print(new_sentence)
