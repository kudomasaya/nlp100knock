# coding:utf-8

str = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
arr = str.translate({ord(","): None, ord("."): None}).split(" ")

res = []

for w in arr:
    res.append(len(w))

print res
