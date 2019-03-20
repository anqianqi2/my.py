'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

def transform_number(l):

    num = 0
    for index,i in enumerate(l):
        num1 = i*pow(10,index)
        num = num1 + num
    return num


def transform_list(num1,num2):
    num = num1 + num2
    list1 = []
    while num > 0:
        i = num % 10
        list1.append(i)

        num = num // 10
    return list1




if __name__ == '__main__':
    l1 = [2, 6, 8]
    l2 = [3, 5, 9]
    num1 = transform_number(l1)
    num2 = transform_number(l2)
    print(l1,l2)

    list = transform_list(num1,num2)
    print(list)


