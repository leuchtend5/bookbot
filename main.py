def main():
    with open("books/frankenstein.txt") as f:
    report = print_report(chars)
        file_contents = f.read()
        words = file_contents.split()

        count_characters(file_contents)

def count_characters(characters):
    chars_dict = {}
    lowercase_chars = characters.lower()

    for char in lowercase_chars:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

    print(chars_dict)

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
