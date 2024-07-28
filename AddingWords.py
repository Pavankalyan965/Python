words = []
word = input("Enter a word:")

while word != "":
    if word not in words:
        words.append(word)
        word = input("Enter a word, blank line to quit:")

for word in words:
    print(word)
