'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

import  math
def longestPalindrome(str):
    list = []
    s = ''

    for i in range(len(str)):
        for j in range(len(str),-1,-1):
            str1 = str[i:j]
            #str1 = str[i:i+1]
            #print(str1)
            count = 0
            for x in range(len(str1)//2):

                #print (x)
                opposite = str1[len(str1)-1 - x]
                #print(opposite)
                if str1[x] == opposite:
                    count += 1
                else:
                    break
            if count == math.floor(len(str1)/2) and len(str1) > len(s):
                s = str1

    return s



if __name__ == '__main__':
    str = 'asdsa'
    print(longestPalindrome(str))

















