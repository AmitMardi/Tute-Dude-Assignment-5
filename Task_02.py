# Task 2: Demonstrate List Slicing

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list: {}".format(my_list))
list_of_five = my_list[:5]
print("Extracted first five elements: {}".format(list_of_five))
list_of_five.reverse()
print("Reversed extracted elements: {}".format(list_of_five))