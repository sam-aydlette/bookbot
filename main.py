def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_chars_dict(text)
    char_sorted = chars_dict_to_sorted_list(char_count)

    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("---End Report---")

    
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    letter_count = {}
    for c in text:
        lowered_text = c.lower()
        if lowered_text in letter_count:
            letter_count[lowered_text] += 1
        else:
            letter_count[lowered_text] = 1
    
    return letter_count

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()