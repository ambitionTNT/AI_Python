# python learing
# author:TNT
num = int(input("请输入星星的层数:"))
for i in range(num):
    for j in range(i+1):
        print("*",end='')
    print()


row = num

for i in range(num):
    for j in range(row-1):
        print(" ",end="")
    row -= 1
    for n in range(i+1):
        print("*",end='')
    print()

row = num

for i in range(num):
    for j in range(row-1):
        print(" ",end='')
    row -= 1
    for n in range(i*2+1):
        print("*",end='')
    print()


