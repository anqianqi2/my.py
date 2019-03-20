'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

'''
def convert(s, numRows):
  n = len(s)
  list = []
  sept = 2*numRows -2
  for i in range(numRows):
      x = i
      y = -i

      while x < n or y < n :
          if i != 0 and i != (numRows-1) and y > 0:
              list.append(s[y])
          if x < n:
              list.append(s[x])
          x += sept
          y += sept
  return ''.join(list)

if __name__ == '__main__':
    s = "LEETCODEISHIRING"
    num = 4
    print(convert(s,num))


