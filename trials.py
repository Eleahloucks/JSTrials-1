"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)



def get_all_evens(nums):
    for num in nums:
        if num % 2 == 0:
            return num


def get_odd_indices(items):
    result =[]
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(i)
    return result


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i += 1




def get_range(start, stop):
    nums=[]

    for i in range(start, stop):
        nums.append(i)

    return nums




def censor_vowels(word):
    letters = []
    for letter in word:
        if letter in "aeiou":
            letter == '*'
        letters.append(letter)
    return "".join(letters)

def snake_to_camel(string):
    camel_case=[]
    for word in string.split("_"):
        camel_case.append(f"{word[0].upper()}" + f"{word.slice[1:]}")
    return "".join(camel_case)

def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


def truncate(string):
    result=[]
    for character in string:
        if len(result) == 0 or character != result[len(result)-1]:
            result.append(character)
    return "".join(result)


def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

        if parens < 0:
            return False

    return parens == 0


def compress(string):
    compress=[]
    current_char=""
    char_count=0

    for character in string:
        if character != current_char:
            compress.append(current_char)

        if char_count >1:
            compress.append(str(char_count))
        current_char = character
        char_count = 0

    char_count += 1
    compress.append(current_char)

    if char_count > 1:
        compress.append(str(char_count))

    return "".join(compress)


