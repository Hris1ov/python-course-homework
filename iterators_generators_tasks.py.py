# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write an EvensIterator class, such that its objects can be used in for loops, iterating over the even numbers in specified [start, end] range (both inclusive).
"""

# class EvensIterator:
#     def __init__(self, start, end):
#         if start % 2 == 0:
#             self.current = start
#         else:
#             self.current = start + 1
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         value = self.current
#         self.current += 2
#         return value

# ### TEST:
# for x in EvensIterator(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a generator function (evens_generator), such that will yield an even number
in specified [start, end] range (both inclusive).
"""

# def evens_generator(start, end):
#     if start % 2 != 0:
#         start += 1
    
#     current = start
#     while current <= end:
#         yield current
#         current += 2


# ### TEST:
# for x in evens_generator(1,20):
#     print(x, end=",")


### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Define a generator function which will yield all Cyrillic Upper Letters, starting from 'А', to 'Я'
Tip: you can get a letter form its code, using the chr() built-in function, as shown in next examples:
print( chr(1040) )
# 'А''
print( chr(1041) )
# 'Б'
print( chr(1071) )
# 'Я'
"""

# def cyrillic_metodic_upperic_letteric():
#     for char in range(1040,1072):
#         yield chr(char)


# # TEST:
# for l in cyrillic_metodic_upperic_letteric():
#     print(l, end=",")

### EXPECTED OUTPUT:
# А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я,

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create both a generator function (words_from_sentence) and an iterator class (WordsFromSentence) that produces words from a sentence. Both should split the input sentence by 
spaces and return each word, one at a time when iterated over. Your implementation should handle empty sentences properly.
"""


def words_from_sentence(sentence):
    for w in sentence.split():
        yield w


# # TEST case 1: Using the iterator class
# print("Test with iterator class:")
# for w in WordsFromSentence("this is a test"):
#     print(w)

# class WordsFromSentence:
#     def __init__(self, sentence):
#         self.words = sentence.split()
#         self.index = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index < len[self.words]:
#             word = self.words[self.index]
#             word += 1
#             return word
#         else:
#             raise StopIteration


# # # TEST case 2: Using the generator function
# print("\nTest with generator function:\n")
# for w in words_from_sentence("this is a test"):
#     print(w)

### EXPECTED OUTPUT:
# Test with iterator class:
# this
# is
# a
# test
#
# Test with generator function:
# this
# is
# a
# test