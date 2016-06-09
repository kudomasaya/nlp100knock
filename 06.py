# coding:utf-8


def get_ngram(seq, n):
    arr = []
    if isinstance(seq, str):
        arr = seq.split(" ")
    else:
        arr = list(seq)

    # 単語n-gram
    word_result = [arr[i:i+n] for i in range(0, len(arr))]

    # 文字n-gram
    char_arr    = list(''.join(arr))
    char_result = [''.join(char_arr[i:i+n]) for i in range(0, len(char_arr))]

    return {'word': word_result, 'char': char_result}


def main():
    x = set(get_ngram("paraparaparadise", 2)['char'])
    y = set(get_ngram("paragraph", 2)['char'])

    print 'x = ' + str(x)
    print 'y = ' + str(y)

    print 'x | y = ' + str(x | y)
    print 'x & y = ' + str(x & y)
    print 'x - y = ' + str(x - y)

    print 'x in se = ' + str('se' in x)
    print 'y in se = ' + str('se' in y)

if __name__ == '__main__':
    main()
