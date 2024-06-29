def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book_file(book_path)
    word_count = count_words(book_text)
    letter_count_dict = count_letters(book_text)
    # print(book_text)
    # print(word_count)
    print(letter_count_dict)

def count_words(text):
    words = text.split()
    return len(words)

def read_book_file(path):
    with open(path) as f:
        return f.read()

def count_letters(text):

    letters = {}

    for word in text:
        lower_word = word.lower()

        for char in lower_word:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

    return letters



main()
