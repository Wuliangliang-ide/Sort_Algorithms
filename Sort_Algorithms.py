

def bubbleSort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


def Merge_Sort(aList: list) -> list:
    '''
    归并排序原理为：
        将列表的所有元素都2分为一个个的子列表，一直进行2分，直到只剩下一个元素的子列表。也就是说，有多少个元素，就有多少个子列表。
        然后对每两个子列表就行排序，返回该子列表的父列表（这个父列表是该子列表上上次二分下来的子列表）。
        重复进行排序操作，最终返回原列表。
    :param aList:一个列表
    :return:列表
    '''
    if len(aList) > 1:
        mid = len(aList) // 2
        left = aList[:mid]
        right = aList[mid:]

        Merge_Sort(left)  # 递归二分左边列表
        Merge_Sort(right)  # 递归二分右边列表

        i = j = k = 0  # i为左边列表的索引，j为右边列表索引，k为aList的索引
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                aList[k] = left[i]
                i += 1
            else:
                aList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            aList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            aList[k] = right[j]
            j += 1
            k += 1
    return aList


def Quick_Sort(aList: list) -> list:
    if len(aList) <= 1:
        return aList
    else:
        mid = len(aList) // 2
        mid_num = aList[mid]
        aList.remove(mid_num)
        left, right = [], []

        for num in aList:
            if num >= mid_num:
                right.append(num)
            else:
                left.append(num)
        return Quick_Sort(left) + [mid_num] + Quick_Sort(right)

