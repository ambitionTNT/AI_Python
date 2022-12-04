# python learing
# author:TNT
import collections
from collections import Counter
import re
text = 'remove an existing key one level down remove an existing key one level down'
words = re.findall(r'\w+', text)

print(Counter(words).most_common(10))

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)

L = ['red', 'blue', 'red', 'green', 'blue', 'blue']
C = Counter(L)
list1 = list(C.elements())
print(list1)
print(C.most_common(1))


c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)

print(c)



str = Counter('aabbccddss')
print(str)
str.subtract('abcd')
print(str)
