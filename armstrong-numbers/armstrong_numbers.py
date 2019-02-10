def is_armstrong(number):
    
    value = str(number)
    value_size = len(value)
    total = 0
    for e in value:
        total += int(e)**value_size
    return total == number
