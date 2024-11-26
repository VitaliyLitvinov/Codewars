words = ['hello', 'world', 'this', 'is', 'great']
def smash(words):
    sentence = ''
    for i in words:
        sentence += (i + ' ')
    return sentence[0:-1]
print(smash(words))