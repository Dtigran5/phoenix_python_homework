word = ["apple", "hello", "good", "orange",]
if len(word) == len(set(word)):
    print("words are unique")
else: 
    print("words are not unique. there are duplicate words")