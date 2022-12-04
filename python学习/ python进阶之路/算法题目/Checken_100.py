# python learing
# author:TNT
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
'''暴力解法'''
for  x in range(20):
    #公鸡数目
    for n in range(int(100/3)):
        z = 100 - x - n
        if 5 * x + 3 * n + z // 3 == 100 and z % 3 == 0 :
            print(x,n,z)


