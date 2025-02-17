# simple python drill that uses dictionary to translate number into words
# example: 123 -> one two three 
numbers = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

output = ""
number = input('Phone: ')
for digit in number:
    output = output + " " + numbers[digit]

print(output)