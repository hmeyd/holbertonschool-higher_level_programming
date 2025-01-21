#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(len(my_list)):
        k = 1
        for j in range(i):
            if my_list[j] == my_list[i]:
                    k = 0
        if (k == 1):
            sum = sum + my_list[i]
    return sum
