# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 16:45
# @Author  : Lixun
# @Email   : lixunpost@163.com
# @File    : test.py
# @Software: PyCharm

def read_text(name):
    line = []
    with open(name) as f:
        a = f.readlines()
    for i in a:
        k = i.strip().replace('省','')
        if k not in line and k:
            line.append(k)
    return line

if __name__ == '__main__':
    a = read_text('11.txt')
    b = read_text('22.txt')
    c = read_text('33.txt')
    print(sorted(set(a)))
    print(sorted(set(b)))
    # print(sorted(set(c)))
    for i in set(b):
        if i not in a:
            print(i)
    print(len(set(a)))
    print(len(set(b)))
