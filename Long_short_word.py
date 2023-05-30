def find_long_short_words(sentence):
    words = sentence.split()
    long_words = max(words,key=len)
    short_words = min(words,key=len)
    return long_words,short_words

sentence = input("Enter a sentence : ")
long_words , short_words = find_long_short_words(sentence)
print("The longest word :",long_words)
print("The shortest word :",short_words)

