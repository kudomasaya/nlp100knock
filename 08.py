# coding:utf-8


def cifier(string):
    return ''.join(chr(219 - ord(c)) if c.islower() else c for c in string)


def main():
    string = "Hello, world!"
    print cifier(string)
    print cifier(cifier(string))

if __name__ == '__main__':
    main()
