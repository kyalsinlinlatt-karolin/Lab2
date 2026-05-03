def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    num = input()
    num_str_list = num.split(", ")                        # to get the list
    print("String list = ", num_str_list)
    num_float_list = []
    for x in num_str_list:                               #change the string to float
        num_float_list.append(float(x))
    print(f"Float list = {num_float_list}")
    return num_float_list


def calc_average(num_float_list):
    print("calc_average")
    average = sum(num_float_list)/len(num_float_list)
    print(f"    The average is {average}")
    return average

def find_min_max(num_float_list):
    print("find_min_max")
    copy_num_float_list = num_float_list.copy()
    copy_num_float_list.sort()
    return[copy_num_float_list[0], copy_num_float_list[-1]]    # array[-1] gives the last element of the list


def sort_temperature(num_float_list):
    print("sort_temperature")
    copy_list = num_float_list.copy()
    copy_list.sort()
    return(copy_list)

def calc_median_temperature(num_float_list):
    print("calc_median_temperature")
    temp_list_for_median = num_float_list.copy()
    temp_list_for_median.sort()
    count_list = len(temp_list_for_median)
    if count_list%2 == 1:                             #The reminder will be 1, so the number of items is odd
        median = temp_list_for_median[count_list//2]  #Calling array --> taking the middle number --> if "/", you will get float, so use "//" 
                                                      #indexing starts from 0, so no need to add like normal maths
    else:
        median = (temp_list_for_median[count_list//2] + temp_list_for_median[count_list//2 - 1])/2
    return median


def main():
    print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()

    num_list = get_user_input() #The main number list (Float list)

    average_value = calc_average(num_list)
    min_max_list = find_min_max(num_list)
    print(f"    The Min and Max list is {min_max_list}")
    sorted_list =  sort_temperature(num_list)
    print(f"    The sorted temperature list is {sorted_list}")
    median_temp = calc_median_temperature(num_list)
    print(f"    The median temperature is {median_temp}")

if __name__ == "__main__": 
    main() 

    