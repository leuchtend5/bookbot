def main():
    path = "books/frankenstein.txt"
    book_string = read_books(path)
    words = count_words(book_string)
    chars = count_characters(book_string)
    report = print_report(chars)

        

def read_books(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(string):
    words = string.split()
    return len(words)



def count_characters(characters):
    chars_dict = {}
    lowercase_chars = characters.lower()

    for char in lowercase_chars:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

    return chars_dict

def print_report(words_dict):
    chars_list = []

    for char in words_dict:
        if char.isalpha():
            chars_list.append({"char": char, "count": words_dict[char]})

    chars_list.sort(reverse=True, key=sort_on)

    for chars in chars_list:
        print(f"The '{chars['char']}' character was found {chars['count']} times")


def sort_on(dict):
    return dict["count"]


main()
