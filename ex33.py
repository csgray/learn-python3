def while_list(maximum, step = 1):
    i = 0
    numbers = []
    
    # Executes this code block so long as the condition is true
    while i < maximum:
        print(f"At the top i is {i}")
        numbers.append(i)

        # Increments the variable so that the loop eventually exits
        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

while_list(5)
while_list(10, 2)

# A while loop can do anything, but a for loop is often better
def for_list(maximum, step = 1):
    numbers = []

    for i in range(0, maximum, step):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")
    
    for num in numbers:
        print(num)

for_list(6)
for_list(12, 3)