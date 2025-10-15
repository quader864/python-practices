number=0
index=0
if not (n := input().strip()):
    print("invalid")
else:
    list_of_words=n.split(" ")
    for word in list_of_words:
        if number<len(word):
             number=len(word)
             index=word

    print(index)
