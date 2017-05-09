

def maxi(n1, n2):
    #  Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else
    # construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is 
    # nevertheless a good exercise.)
    return(n1) if n1 > n2 else return(n2)


def max_of_three(n1, n2, n3):
    #  Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
    if n1 > n2 and n1 > n3:
        return(n1) 
    elif n2 > n1 and n2 > n3:
        return(n2)
    else:
        return(n3)


def lenght(list_string):
    #  Define a function that computes the length of a given list or string. (It is true that Python has the len() 
    # function built in, but writing it yourself is nevertheless a good exercise.)
    lenght = 0
    for i in list_string:
        lenght += 1
    return(lenght)


def is_vowel(character):
    #  Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel,
    # False otherwise.
    return(True) if character in 'aeiou' else return(False)


def rövarspråket(text):
    #  Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
    # That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") 
    # should return the string "tothohisos isos fofunon".
    rövar = []
    for letter in text:
        if letter in 'aeiou':
            rövar.append(letter)
        else:
            rövar.extend((letter, 'o', letter))
    return(''.join(rövar))


def sum_nums(nums_list):
    # Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a
    # list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
    sums = 0
    for num in nums_list:
        sums = sums + num
    return(sums)


def multiply(nums_list):
    multi = 1
    for num in nums_list:
        multi = multi * num
    return(multi)


def rev(string):
    #  Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") 
    #  should return the string "gnitset ma I".
    string_as_list = list(string)
    reverse_list = []
    reverse_list.append(string_as_list[-1])
    lenght = len(string)
    count = 2
    for char in string_as_list:
        reverse_list.append(string_as_list[lenght-count])
        count += 1
    reverse_string = str(reverse_list)
    return(reverse_list)


def is_palindrome(string):
    #  Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
    # For example, is_palindrome("radar") should return True.
    rev_str = reversed(string)
    if list(string) == list(rev_str):
        return(True)
    else:
        return(False)


def member(value, some_list):
    #  Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
    # and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
    # but for the sake of the exercise you should pretend Python did not have this operator.)
    for i in some_list:
        if i == value:
            return True
    return False



