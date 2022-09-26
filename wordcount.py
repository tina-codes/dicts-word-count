"""Count words in file."""


# put your code here.
def count_words(input_file):

    word_count = {}

    for line in input_file:
        for word in line:
            word_count[word] = word_count.get(word, 0) + 1

with open("test.txt") as input_file:
    count_words(input_file)

