# Module where some functions will be stored

# Function that finds the maximum number from the given list
def find_max(numbers_list):
    max = numbers_list[0]

    for i in numbers_list:
        if max < i:
            max = i
    
    return max