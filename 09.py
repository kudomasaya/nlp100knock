# coding:utf-8
import random


def main():
    txt = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    arr = txt.split(" ")
    res = []
    for w in txt.split(" "):
        if len(w) > 4:
            t = list(w)
            f = t.pop(0)
            l = t.pop()
            random.shuffle(t)
            w = f + ''.join(t) + l
        res.append(w)
    print ' '.join(res)

if __name__ == '__main__':
    main()
