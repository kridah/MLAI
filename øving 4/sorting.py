import random
import string
import datetime as date


# REFERANSER
# Hands-On Data Structures and Algorithms with Python
# https://pynative.com/python-generate-random-string/
# https://www.geeksforgeeks.org/python-program-convert-string-list/

# converterer en strint til en list
def convert(string):
    my_list = []
    my_list[:0] = string
    return my_list

# oppgave 1
# Lag en funksjon som returnerer et randomgenerert array av strenger.
# Størrelsen skal angis som parameter
def random_string_generator(length):
    letters = string.ascii_letters.upper()
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("List of length ", length, "is to be sorted ")
    return result_str


# Bruk rutinen fra Oppgave 1 og sorter arrayet vha Boblesortering
def bubblesort(unordered_list):
    iteration_number = len(unordered_list) - 1
    for i in range(iteration_number):
        for j in range(iteration_number):
            if unordered_list[j] > unordered_list[j + 1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j + 1]
                unordered_list[j + 1] = temp
    return unordered_list


def insertionsort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]

        while search_index > 0 and unsorted_list[search_index-1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1

        unsorted_list[search_index] = insert_value
    return unsorted_list


# selection sort nekter å kjøre 100.000 elementer
def selectionsort(unsorted_list):
    size_of_list = len(unsorted_list)

    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
    return unsorted_list


# def mergesort(unsorted_list):
#     if len(unsorted_list) == 1:
#         return unsorted_list
#
#     mid_point = int(len(unsorted_list) / 2)
#
#     first_half = unsorted_list[:mid_point]
#     second_half = unsorted_list[mid_point:]
#
#     half_a = mergesort(first_half)
#     half_b = mergesort(second_half)
#
#     return merger(half_a, half_b)

# def merger(first_sublist, second_sublist):
#     i = j = 0
#     merged_list = []
#
#     while i < len(first_sublist) and j < len (second_sublist):
#         if first_sublist[i] < second_sublist[j]:
#             merged_list.append(first_sublist[i])
#             i += 1
#         else:
#             merged_list.append(second_sublist[j])
#             j += 1
#
#     while i < len(first_sublist):
#         merged_list.append(first_sublist[i])
#         i += 1
#
#     while j < len(second_sublist):
#         merged_list.append(second_sublist[j])
#         j += 1
#
#     return merged_list


random_string = random_string_generator(10000)
random_list = convert(random_string)

# start_time = date.datetime.now()
# bubblesort(random_list)
# end_time = date.datetime.now()
# used_time = end_time - start_time
# print("Bubblesort:   ", used_time)


# start_time = date.datetime.now()
# insertionsort(random_list)
# end_time = date.datetime.now()
# used_time = end_time - start_time
# print("Insertin sort:", used_time)
# start_time = date.datetime.now()
# #mergesort(random_list)
# end_time = date.datetime.now()
# used_time = end_time - start_time
# print("Merge sort:", used_time)

# start_time = date.datetime.now()
# selectionsort(random_list)
# end_time = date.datetime.now()
# used_time = end_time - start_time
# print("Selection sort:", used_time)

from sorting_visualizer import visualizer
visualizer.visualize('mergesort')
