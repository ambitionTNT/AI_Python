# python learing
# author:TNT
"""迭代工具模块"""
import itertools

for i in itertools.combinations_with_replacement('1234',2):
    print(i)

#产生ABCD的全排列

for i in itertools.permutations('ABCD'):
    print(i)

#产生ABCDE的五选三组合
for i in itertools.combinations('ABCDE', 3):
    print(i)
#产生ABCD和123的笛卡尔积
for i in itertools.product('ABCD','123'):
    print(i)

#产生无限循环的序列
# for i in itertools.cycle(('A', 'B', 'C')):
#
#     print(i)


for i in itertools.chain('good','hello'):
    print(i)





