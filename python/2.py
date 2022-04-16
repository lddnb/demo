'''
Author: your name
Date: 2022-04-14 10:56:29
LastEditTime: 2022-04-16 15:54:14
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Leetcode\python\2.py
'''
import copy

arr1 = [1, 2, 3]

arr3 = [4, 5, 6, arr1]
arr4 = copy.deepcopy(arr3)
arr4[-1][-1] = 9
print(arr1)
print(arr3)
print(arr4)
