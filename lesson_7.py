"""
Linked List [] - нужен для сортировки и чтобы было удобно
Hash Map -
"""

"""
Selection Sort
"""

""" Hash Map"""
""" key == Hash Function"""
""" value == Hash value"""

# dict_ = {
#     "jack": 20,
#     "barbaro":25,
#     "beknazar": 15,
#     "islambek": 19,
#
# }
# name = input()
# print(dict_[name])
# # for key in dict_:
# #     if key == name:
#         print(dict_[key])

""" Big 0 (1)"""

""" Algorithm"""
#
# elems = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -4, -6, -3, -2]
#
# for index_one in range(len(elems)):
#     for index_two in range(index_one, len(elems)):
#         if elems[index_one] > elems[index_two]:
#             elems[index_one], elems[index_two] = elems[index_two], elems[index_one]
#
# print(elems)

""" Big O(n^n)"""


mass = [[[[[[[[[0, 15, 10]]]]]]]]]

def recursive(arr):
    if arr.__len__() > 1:
        try:
            elem_index = arr.index(15)
            print(f"15 index = {elem_index}")
        except IndexError:
            print("Elem not found")
    else:
        recursive(arr[0])

recursive(mass)




