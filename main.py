def main():
    with open("books/frankenstein.txt") as f:
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

main()
