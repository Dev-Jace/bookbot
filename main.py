
# book_title = "frankenstein"
# print(f"books/{book_title}.txt")

# books-start
frankenstein = "frankenstein"

# books-end

def read_book(book_title):
    book_location = f"books/{book_title}.txt"
    #print( isinstance(book_location, str) )
    with open(book_location) as f:
        return f.read()
#
def char_count(txt_string):
    unic_char =  {} #set()
    txt_string = txt_string.lower()
    #unic_char_count = []

    for character in txt_string:
        if character not in unic_char:
            unic_char[character] = 1
        else:
            unic_char[character] +=1

    return unic_char
#
def ttl_word_count(txt_string):
    word_count = txt_string.split()
    return len(word_count)
#
def print_alpha_values(char_dict):
    dict_char = {}
    dict_char_index =[]

    for char in char_dict:
        if char.isalpha():
            dict_char[char_dict[char]] = char
            dict_char_index.append(char_dict[char])

    dict_char_index.sort(reverse=True)
    for index in dict_char_index:
        print(f"The '{dict_char[index]}' character was found {index} times")
    return
    





def main():
    # 
    book = frankenstein
    print(f"--- Begin report of books/{book}.txt ---")
    print(f"{ttl_word_count(read_book(book))} words found in the document.")
    print()
    print_alpha_values(char_count(read_book(book)))
    print("--- End report ---")
    return 

# old main -start
def main_read():
    print(read_book(frankenstein))
    return
# old main -end


main()

def test():
    txt_string = "today is a day"
    
    unic_char =  {} #set()
    txt_string = txt_string.lower()
    #unic_char_count = []

    for character in txt_string:
        if character not in unic_char:
            unic_char[character] = 1
        else:
            unic_char[character] +=1
    
    for entry in unic_char:
        print(f"{entry} : {unic_char[entry]}" )

#test()



"""
with open("books/frankenstein.txt") as f:
    print(f.read() )
"""
