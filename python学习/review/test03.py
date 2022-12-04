# python learing
# author:TNT
"""输入两个正整数，计算它们的最大公约数和最小公倍数。"""

x = int(input("请输入第一个整数"))
y = int(input("请输入第二个整数"))

# 如果x大于y就交换x和y的值
if x>y :
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x,y = y,x
for factor in range(x,0,-1):
    if x%factor == 0 and y % factor ==0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
