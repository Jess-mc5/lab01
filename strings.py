strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for s in range(len(strings)):
    sentence = sentence + strings[s] + " "

print(sentence[:-1])

print(' '.join(strings))
