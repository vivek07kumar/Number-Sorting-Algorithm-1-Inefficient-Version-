# Smallest to Greatest Sorting
    # >> Logic behind the algorithm is as follows -:
    # 1. Find the smallest number among the user give list.
    # 2. Make a new list with include this smallest number or any smallest number after.
    # 3. Then update user list so that it no longer include the previous smallest number.
    # >> Repeat this process n number of times, where n is the length of the actual user list.
# Removing Duplicates
    # 1. step 1 -: Take a number from user given list and place it in a new list.
    # 2. step 2 -: The take another number from user list and try matching its equality with elements of new list. If it matches then don't place it in new list. If it matches then place it in user list.
    # 3. Repeat the step 1 and step 2 until matching of all the numbers of user list is completed. New list will be the Non diplicate list.
def non_duplicate_list_function(user_list) :
    # Removing duplicates
    duplicate_list = user_list[:]
    non_duplicate_list = []
    duplicate_check = False
    duplicate_check_2 = True
    for variable_1 in duplicate_list :
        if non_duplicate_list == [] :
            non_duplicate_list = non_duplicate_list + [variable_1]
        else :
            for variable_2 in non_duplicate_list :
                if variable_1 != variable_2 :
                    duplicate_check = True
                else :
                    duplicate_check = False
                    duplicate_check_2 = False
        if duplicate_check and duplicate_check_2 :
            non_duplicate_list = non_duplicate_list + [variable_1]
        duplicate_check_2 = True
    return non_duplicate_list
def number_sorting_function (user_list) :
    # smallest to greatest
    result_list = []
    new_list = []
    smallest_number = user_list[0]
    num = 1
    numbers_of_element = 0
    result_01 = non_duplicate_list_function(user_list)
    list_length = len(result_01)
    while num <= list_length :
        for x in user_list :
            if x < smallest_number :
                smallest_number = x
        for x in user_list :
            if x == smallest_number :
                numbers_of_element = numbers_of_element + 1
        result_list = result_list + ([smallest_number] * numbers_of_element)
        for x in user_list :
            if x > smallest_number :
                new_list = new_list + [x]
        user_list = new_list[:]
        new_list = []
        if len(user_list) > 0 :
            smallest_number = user_list[0]
        num = num + 1
        numbers_of_element = 0
    return result_list
def number_sorting_function_2(user_input) :
    # Greatest to Smallest
    list_02 = user_input[:]
    list_length = len(list_02)
    index = -1
    number = 1
    greatest_to_smallest_list = []
    while number <= list_length :
        greatest_to_smallest_list = greatest_to_smallest_list + [list_02[index]]
        index = index - 1
        number = number + 1
    return greatest_to_smallest_list
def main() :
    user_input = eval(input('>> Please enter numbers seperated by comma : '))
    user_list = list(user_input)
    print()
    result_1 = number_sorting_function(user_list)
    print()
    print('>> Smallest to Greatest ---->  ',result_1)
    print()
    result_3 = number_sorting_function_2(result_1)
    print('>> Greatest to Smallest ---->  ',result_3)
    print()
    result_2 = non_duplicate_list_function(user_list)
    result_2 = number_sorting_function(result_2)
    print('>> After Removing Duplicate Number/s ---->  ',result_2)
    print('   Number of Duplicate Element/s found ----> ',len(user_list) - len(result_2),'Element/s')
    print()
main()
