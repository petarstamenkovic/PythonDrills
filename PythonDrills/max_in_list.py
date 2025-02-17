# simple python program that finds the largest number in the given list

#numbers = [1,4,76,8,3,6,66,845,13,441]
def find_max(numbers_list):
    max = numbers_list[0]

    for i in numbers_list:
        if max < i:
            max = i
    
    return max

#print(f"Biggest number in the list is: {max}")