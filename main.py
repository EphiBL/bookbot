def main():
    book_path = "books/frankenstein.txt"

    book_text: str = read_book_file(book_path)
    word_count: int = count_words(book_text)
    character_frequencies: dict = count_characters(book_text)
    frequencies: list = list_letters(character_frequencies)
    frequencies.sort(reverse=True, key=sort_on)

    print(f"--- Begin Report of {book_path}  ---")
    print(f"There are {word_count} words in the book")
    print(" ")

    for letter in frequencies:
        print(f"The '{letter['name']}' character occurs {letter['num']} times")

    print("--- End Report ---")

def count_words(text):
    words = text.split()
    return len(words)

def read_book_file(path):
    with open(path) as f:
        return f.read()

# Returns "num" k:v of dict
def sort_on(dict):
    return dict["num"]

def list_letters(char_frequencies: dict) -> list:
    letters_list = []

    for char in char_frequencies:
        if char.isalpha():
            letter_dict = {
                "name": char,
                "num": char_frequencies[char]
            }
            letters_list.append(letter_dict)

    return letters_list

def count_characters(text):
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
