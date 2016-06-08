# coding:utf-8

str = u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
arr = str.translate({ord(","): None, ord("."): None}).split(" ")

res = {}

for i in range(0, len(arr)):
    key = i + 1
    if key in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        res[key] = arr[i][0:1]
    else:
        res[key] = arr[i][0:2]

print res
