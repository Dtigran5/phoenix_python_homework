text = input("input text: ")
char = input("input specific char that you want to count: ")

char_count = {}

for i in text:
    char_count[i] = char_count.get(i, 0) + 1

count = char_count.get(char, 0)

print(f"the character '{char}' in text '{text}' occurs {count} times")