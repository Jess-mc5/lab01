strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

x = 0
for string in strings:
    print(strings[x], end = " ")
    x = x + 1

print(sentence)

print(' '.join(strings))
