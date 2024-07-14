file = open("Week 7/test.txt","r")
strings = file.read()
print(strings)
search_word = input("enter a word you want to search in file: ")
if(search_word in strings):
    print("word found is: "+search_word)

else:
    print("word not found")
