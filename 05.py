# coding:utf-8

def getNgram(seq, n):
    arr = []
    if isinstance(seq, str):
        arr = seq.split(" ")
    else:
        arr = list(seq)

    #単語n-gram
    #{I-am am-an an-NLPer}
    res = []

    #文字n-gram
    #{Ia,am,ma,an,nN,NL,LP,Pe,er,r}

    print arr
    return {}

def main():
    #str = "I am an NLPer"
    str = ["I","am","an","NLPer"]
    res = getNgram(str, 2)
    print res

if __name__ == '__main__':
    main()
