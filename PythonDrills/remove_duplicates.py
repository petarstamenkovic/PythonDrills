# Simple Python drill that removes the duplicated from a given list

numbers = [1,3,4,55,1,3,57,9,0]
print(f"Original list: {numbers}")

for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)

print(f"Modified list: {numbers}")