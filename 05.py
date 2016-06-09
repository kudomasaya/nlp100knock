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
    char_result = [char_arr[i:i+n] for i in range(0, len(char_arr))]

    return {'word': word_result, 'char': char_result}


def main():
    s = "I am an NLPer"
    res = get_ngram(s, 2)
    print res

if __name__ == '__main__':
    main()
