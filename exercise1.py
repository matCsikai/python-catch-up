def get_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def get_max_from_list(num_list):
    max_num = num_list[0]
    
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num
                   


