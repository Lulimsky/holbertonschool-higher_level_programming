#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    index_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index_list.append(i)
                    index_list.append(j)
    print(list(set(index_list)))
    return index_list
