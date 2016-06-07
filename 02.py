# coding:utf-8

str1 = u"パトカー"
str2 = list(u"タクシー")
res  = ""

for s1 in str1:
    res += s1 + str2.pop(0)

print res.encode('utf-8')
