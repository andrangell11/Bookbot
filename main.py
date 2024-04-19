def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    counted_words = count_words(file_contents)
    characters_dict = dicto_chars(file_contents)
    list_dict = list_of_dicts(characters_dict)
    sorted_list = list_dict.copy()
    sorted_list.sort(reverse=True, key=sort_on)
    
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counted_words} words found in the document")

    for dict in sorted_list:
        char = dict["character"]
        num = dict["number"]
        if char.isalpha():
            print(f"The {char} character was found {num} times")
    
    print("--- End of report ---")

def count_words(file_contents):
    words = file_contents.split()    
    return len(words)

def dicto_chars(file_contents):
    lower_case_file_contents = file_contents.lower()
    characters = {}
    for c in lower_case_file_contents:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def list_of_dicts(characters_dict):
    list = []
    for key in characters_dict:
        list.append({"character": key, "number": characters_dict[key]})
    return list

def sort_on(list_dict):
    return list_dict["number"]    




main()