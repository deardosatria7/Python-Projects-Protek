def sum1(*variabel):
    sum = 0
    for var in variabel:
        sum += var
    return sum


def average(*variabel):
    sum = 0
    i = 0
    for var in variabel:
        sum += var
        i += 1
    hasil = sum/i
    return hasil


def maksimum(*data):
    max_value = data[0]
    for x in data:
        if (max_value < x) :
            max_value = x
    return max_value   

def minimum(*data):
    min_value = max (*data) + 1
    for x in data:
        if (min_value > x) :
            min_value = x
    return min_value


