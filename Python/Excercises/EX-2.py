# Write a program that takes a sentence as input and counts the occurrences of each word in the sentence

def count_word_occurrences(sentence):
    # Convert the sentence into lowercase and split it
    words = sentence.lower().split()

    # create a empty dictionary to store word count
    word_count = {}

    # Count the occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Take input sentence from the user
input_sentence = input("Enter a sentence: ")

# Count occurrences of each word
word_occurrences = count_word_occurrences(input_sentence)

# Print word frequencies
for word, count in word_occurrences.items():
    print(f"'{word}' occurs {count} time(s)")

