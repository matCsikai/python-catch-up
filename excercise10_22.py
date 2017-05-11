def overlapping(list1, list2):
    # Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
    # False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
    # you should (also) write it using two nested for-loops.
    for list1_item in list1:
        for list2_item in list2:
            if list1_item == list2_item:
                return True
    return False

list1 = [1, 'z', 3]
list2 = [3, 4, 'z']
print(overlapping(list1, list2))


def generate_n_chars(integer, character):
    #  Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters
    # long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is
    # unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the
    # exercise you should ignore that the problem can be solved in this manner.)
    count = 0
    same_characters = []
    while count < integer:
        same_characters.append(character)
        count += 1
    character_string = ''.join(same_characters)
    return character_string

print(generate_n_chars(6, "s"))


def histogram(int_list):
    #  Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
    for num in int_list:
        print(num * '*')

int_list = [8, 7, 6]
histogram(int_list)


def get_max_in_list(num_list):
    # Write a function max_in_list() that takes a list of numbers and returns the largest one.
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

print(get_max_in_list([54, 65, 31, 85, 2]))


def word_lenght(word_list):
    #  Write a program that maps a list of words into a list of integers representing the lengths of
    # the corresponding words.
    num_list = []
    for word in word_list:
        num_list.append(len(word))
    return num_list

print(word_lenght(['az', 'ez', 'amaz', 'emez']))


def find_longest_word(word_list):
    #  Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
    return len(max(word_list))

print(find_longest_word(['az', 'ez', 'amaz', 'emez', 'valamikor']))


def filter_long_words(word_list, num):
    #  Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words
    # that are longer than n
    long_words = []
    for word in word_list:
        if len(word) > num:
            long_words.append(word)
    return long_words

print(filter_long_words(['az', 'ez', 'amaz', 'emez', 'valamikor'], 2))

import string

def palindrome_recognizer(sentence):
    #  Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a
    # lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
    # "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the
    # exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
    sentence_list = list(sentence.lower())
    for char in sentence_list:
        if char in string.punctuation or char == ' ':
            sentence_list.remove(char)
    print(sentence_list)
    reversed_sentence = sentence_list[::-1]
    if sentence_list == reversed_sentence:
        return(True)
    else:
        return(False)

print(palindrome_recognizer("Satan, oscillate my metallic sonatasS"))


def pangram(sentence):
    #  A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
    #  The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if
    # it is a pangram or not.
    sentence = sentence.lower()
    char_list = []
    for char in string.ascii_lowercase:
        if char in sentence:
            char_list.append(char)
    char_string = ''.join(char_list)
    if string.ascii_lowercase == char_string:
        return True
    else:
        return False

print(pangram('The quick brown fox jumps over the lazy dog'))


def beersong():
    #  99 bottles of beer on the wall, 99 bottles of beer.
    #  Take one down, pass it around, 98 bottles of beer on the wall.
    #  The same verse is repeated, each time with one fewer bottle.
    #  The song is completed when the singer or singers reach zero.
    #  Your task here is write a Python program capable of generating all the verses of the song.
    beer_bottles = 99
    while beer_bottles > 0:
        print("%d bottles of beer on the wall, %d bottles of beer." % (beer_bottles, beer_bottles))
        print("Take one down, pass it around, %d bottles of beer on the wall." % (beer_bottles - 1))
        beer_bottles -= 1

beersong()


def translate(english_words):
    #  Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
    # "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your
    # Christmas cards from English into Swedish. That is, write a function translate() that takes a list of
    # English words and returns a list of Swedish words.
    dictionary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    swedish_words = []
    for word in english_words:
        swedish_words.append(dictionary[word])
    return swedish_words

print(translate(["merry", "christmas", "and", "happy", "new", "year"]))


def char_freq(string):
    #  Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
    #  Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
    freq_dict = {}
    letter = ''
    for char1 in string:
        letter = char1
        freq_list = []
        for char2 in string:
            if char2 == letter:
                freq_list.append(char2)
        freq_dict[char1] = len(freq_list)
    return freq_dict

print(char_freq("abbabcbdbabdbdbabababcbcbab"))