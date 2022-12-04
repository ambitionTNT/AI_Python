# python learing
# author:TNT
'''寻找水仙花数'''

for i in range(100,1000):
    low = i % 100 % 10
    mid = i % 100 //10
    high = i//100
    if(low ** 3 + mid ** 3 +high ** 3 == i):
        print(i)

