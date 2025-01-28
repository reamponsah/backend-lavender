sentence = "this is the third assignment"
print(sentence)

# Output Sentence Details
print (len(sentence))
words = len(sentence.split())
print(words)
print(sentence.split()[0])
print(sentence.split()[-1])

# Indexing And Slicing
print(sentence[0:3])
print(sentence[-3:])
print(sentence[::-1])

# Modify The Sentence
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","-"))



