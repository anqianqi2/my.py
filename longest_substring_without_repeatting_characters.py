'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


def lengthOfLongestSubstring(str):
    dict = {}
    left = 0
    ans = 0

    for index,items in enumerate(str):
        if items in dict:
            left = left + 1
        dict[items] = index

        ans = max(ans,index-left+1)

    return ans

if __name__ == '__main__':
    s = 'powpikl'
    print(lengthOfLongestSubstring(s))


