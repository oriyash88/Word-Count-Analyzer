import string

filename = input("Enter the name of the text file: ")

try:
    with open(filename, 'r') as file:
        text = file.read().lower()

        # remove punctuation marks from the text
        text = text.translate(text.maketrans('', '', string.punctuation))

        # split the text into words
        words = text.split()

        # count the total number of words
        total_words = len(words)

        # count the frequency of each word
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # print the results
        print("Total words in the file:", total_words)
        print("Word count:")
        for word, count in word_count.items():
            print(word, ":", count)

except FileNotFoundError:
    print("File not found.")
