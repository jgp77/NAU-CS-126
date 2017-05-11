def word_score(string):
    string=string.lower()
    letter_values={
        'a': 1,
        'b': 3,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 2,
        'h': 4,
        'i': 1,
        'j': 8,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 3,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 4,
        'w': 4,
        'x': 8,
        'y': 4,
        'z': 10}
    score=0
    for i in string:
        score=score + letter_values[i]
    return score


def sum_of_for(number):
    sum_of_cubes=0
    for i in range(1, number + 1):
        sum_of_cubes += i**3
    return sum_of_cubes


def sum_of_while(number):
    sum_of_cubes=0
    while number > 0:
        sum_of_cubes += number**3
        number -= 1
    return sum_of_cubes
