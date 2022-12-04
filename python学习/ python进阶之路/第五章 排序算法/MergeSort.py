# python learing
# author:TNT
'''
归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
分割：递归地把当前序列平均分割成两半。
集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。

'''

class Solution(object):

    def merge(self, data, l, r,  rightEnd):
        '''

        :param data: 数据集
        :param tempData:临时数据集
        :param l:左边起点的位置
        :param r:右边起点的位置
        :param RightEnd:右边终点的位置
        :return:无
        '''


        tempData = []#创建临时数组
        leftEnd = r - 1#记录左边终点的位置，假设左右两列挨着
        tmp = l# 存放结果的数组第一个位置
        NumElement = rightEnd - l + 1 #这两列元素总和
        while l <= leftEnd and r <= rightEnd:
            if data[l] <= data[r]:
                tempData.append(data[l])
                l += 1

            else:
                tempData.append(data[r])
                r += 1
        while l <= leftEnd:
            tempData.append(data[l])
            l += 1
        while r <= rightEnd:
            tempData.append(data[r])
            r += 1
        print(tempData)
        for i in range(0, NumElement):
            data[rightEnd] = tempData.pop()
            rightEnd -= 1



    def merge_Sort(self,arr,l,rightEnd):
        '''
        归并排序
        :param arr: 待排序数组
        :param l: 数组左边
        :param rightEnd: 右边
        :return: 拍完后的数组
        '''

        if l < rightEnd:
            m = int((l + rightEnd) / 2)
            self.merge_Sort(arr, l, m)
            self.merge_Sort(arr, m+1, rightEnd)
            self.merge(arr, l, m+1, rightEnd)



    def mSort(self, arr):
        length = len(arr)
        self.merge_Sort(arr, 0, length-1)

arr = [64, 34, 25, 12, 22, 11, 90]
s = Solution()
s.mSort(arr)
print(arr)



