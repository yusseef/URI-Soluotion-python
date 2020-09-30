n = int(input())

while n:
    n -= 1
    text = input().split()

    for i in text:

        if ('oulupukk' in i):

            if len(i) == 10:
                text[text.index(i)] = 'Joulupukki'
            if len(i) == 11:
                text[text.index(i)] = 'Joulupukki.'

    text = ' '.join(text)
    print(text)
