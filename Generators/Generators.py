"""def find_letter_occurrences(words, letter):
    output = []
    for word in words:
        output.append(word.count(letter))
    return output

#print(
 #   find_letter_occurrences(["apple", "banana", "cherry"], "a")
#)

def find_letter_occurrences(words, letter):
    for word in words:
        yield word.count(letter)
words = ["apple", "banana", "cherry"]
letter = "a"
output = find_letter_occurrences(words, letter)

print(next(output))
print(next(output))
print(next(output))
"""
def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))