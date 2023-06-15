

# This cell loads in the 1000 most common words from `1-1000.txt` 
# and puts them in a list called "common_words"
word_file = open("1-1000.txt")
common_word_file = word_file.read()
common_words = common_word_file.split("\n")