
# kode her
from collections import namedtuple
import csv

persons = []
with open("Personer.dta", "r", encoding="ISO-8859-1") as file:
    for line in file:
        p = line.split(";")
        persons.append(p)  # lager en todimensjonal liste


# def add_persons_to_heap(p_list):
#     current_index = len(p_list) - 1
#
#     while current_index > 0:
#         parent_index = round((current_index - 1)/2)     # round to nearest int
#         # swap if the current object is greater than its parent
#         print(p_list[current_index][0], ">", p_list[parent_index][0], p_list[current_index][0] > p_list[parent_index][0])
#         if p_list[current_index][0] > p_list[parent_index][0]:    # compares on lastname
#             temp = p_list[current_index]
#             p_list.insert(current_index, persons[parent_index])
#             p_list.insert(parent_index, temp)
#         else:
#             break
#         current_index = parent_index


size = len(persons)
persons.insert(0, size - 1)
persons.remove(size - 1)

current_index = 0
while current_index < len(persons):
    left_child_index = 2 * current_index + 1
    right_child_index = 2 * current_index + 2

    if left_child_index >= len(persons):    # is heap
        break
    max_index = left_child_index
    if right_child_index < len(persons):
        if persons[max_index][0] > persons[right_child_index][0]:
            max_index = right_child_index

    if persons[current_index] > persons[max_index]:
        temp = persons[max_index]
        persons.insert(max_index, persons[current_index])
        persons.insert(current_index, temp)
        current_index = max_index
    else:
        break

print("Index 0:", persons[0],
       "\nIndex 20000:", persons[20000],
       "\nIndex 40000:",persons[40000],
       "\nIndex 80000:",persons[80000])



