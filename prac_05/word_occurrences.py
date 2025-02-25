"""
Word Occurrences
Estimate: 20 minutes
Actual: 32 minutes
"""
word_to_count = dict()

words = input("Text: ").split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
for word, count in sorted(word_to_count.items()):
    print(f"{word:{len(max(list(word_to_count.keys()), key=len))}} : {count}")
