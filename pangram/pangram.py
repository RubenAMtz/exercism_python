def is_pangram(sentence):
    abc = list("abcdefghijklmnopqrstuvwxyz")
    
    sentence = sentence.lower()
    result = []
    for char in sentence:
        if char in abc and char not in result:
            result.append(char)
    result.sort()
    if result == abc:
        return True
    return False