def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    num = input()
    num_str_list = num.split(", ")
    print(num_str_list)
    num_float_list = []
    for x in num_str_list: #change the string to float
        num_float_list.append(float(x))
    print(num_float_list)
    return num_float_list


def calc_average(num_float_list):
    print("calc_average")
    average = sum(num_float_list)/len(num_float_list)
    print(average)
    return(average)

def find_min_max(num_float_list):
    print("find_min_max")
    copy_num_float_list = num_float_list.copy()
    copy_num_float_list.sort()
    return[copy_num_float_list[0], copy_num_float_list[-1]]


def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__": 
    main() 

    