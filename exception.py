# Simple drill to use while(prompting until no exception) and exceptions

while True:
    try:
        x = int(input("What number is x? "))
    except ValueError:
        print("Sorry, X is not an integer.")
    else:
        break

print(f"X is: {x}")