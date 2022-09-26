"""Count words in file."""

# put your code here.
def count_words(input_file):

    word_count = {}

    for line in input_file:
        words = line.rstrip().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f"{word} {count}")

    return word_count

with open("twain.txt") as input_file:
    count_words(input_file)

