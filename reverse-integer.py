'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


'''

import math
def reverse(int):
    x = abs(int)
    b = 0
    sign = -1 if int < 0 else 1
    while x > 0:
        a = x % 10    # 取余
        x = x // 10   # 取整
        b = b * 10 + a
    res = b * sign
    return res  if b <= 0X7fffffff else 0



if __name__ == '__main__':
    x = 160
    print(reverse(x))