import string

def abbreviate(words):
    for char in words:
        if char not in string.ascii_letters and char not in " ":
            if char is "'":
                words = words.replace(char, '')
            else:
                words = words.replace(char, ' ')

    acronym = ""
    words_list = words.split()
    for word in words_list:
        acronym += word[0].upper()
    return acronym
